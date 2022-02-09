from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostList, PostDetail, PostViewSet
from .views import UserList, UserDetail, UserViewSet
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
     path('<int:pk>/', PostDetail.as_view()),
     path('', PostList.as_view()),
     # 2301
     path('users/', UserList.as_view()),
     path('users/<int:pk>/', UserDetail.as_view()),

     path('api/v1/', include('posts.urls')),
     # 2301
     path('api/v1/rest-auth/', include('rest_auth.urls')),
     path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
     # 0902
     path('api/v1/', include('apka.urls')),
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='post')
urlpatterns = router.urls
