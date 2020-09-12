from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .mixins import SetAuthorOnCreateMixin
from .models import Comment, Follow, Group, Post
from .permissions import IsOwner
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(SetAuthorOnCreateMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]


class CommentView(SetAuthorOnCreateMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs['post_id'])


class GroupView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FollowView(SetAuthorOnCreateMixin, generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']
