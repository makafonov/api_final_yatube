from .serializers import FollowSerializer


class SetAuthorOnCreateMixin:
    def perform_create(self, serializer):
        if isinstance(serializer, FollowSerializer):
            serializer.save(user=self.request.user)
        else:
            serializer.save(author=self.request.user)
