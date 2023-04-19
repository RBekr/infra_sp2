from django.urls import include, path

from .routers import NoPutRouter
from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, TokenAPI, UserSignUpAPI,
                    UserViewSet)

router_v1 = NoPutRouter()
router_v1.register('v1/users', UserViewSet, basename='users')
router_v1.register('v1/titles', TitleViewSet, basename='titles')
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router_v1.register('v1/genres', GenreViewSet, basename='genres')
router_v1.register('v1/categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/auth/signup/', UserSignUpAPI.as_view(), name='signup'),
    path('v1/auth/token/', TokenAPI.as_view(), name='tokens'),
]
