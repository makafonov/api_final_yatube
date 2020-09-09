from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import include, path

from .views import CommentView, FollowView, GroupView, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentView)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('group/', GroupView.as_view(), name='group'),
    path('follow/', FollowView.as_view()),
    path('', include(router.urls)),
]
