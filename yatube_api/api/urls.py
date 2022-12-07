from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'posts'

v1_router = DefaultRouter()
v1_router.register(r'follow', FollowViewSet, basename='follow')
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments'
                   )


jwtpatterns = [
    path('create/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'
         ),
    path('refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
         ),
    path('verify/',
         TokenVerifyView.as_view(),
         name='token_verify'
         ),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/jwt/', include(jwtpatterns)),
]
