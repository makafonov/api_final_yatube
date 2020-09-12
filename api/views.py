from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db.models import Q

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
    serializer_class = PostSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        queryset = Post.objects.all()
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group=group)
        return queryset


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


class FollowView(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Follow.objects.all()
        username = self.request.query_params.get('search', None)
        if username is not None:
            queryset = queryset.filter(
                Q(user__username=username) | Q(following__username=username)
            )
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
