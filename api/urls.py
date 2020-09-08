from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import include, path

from .views import CommentView, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
