from rest_framework import viewsets

from .mixins import PerformMixin
from .models import Comment, Post
from .permissions import IsOwner
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(PerformMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner, )


class CommentView(PerformMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs['post_id'])
