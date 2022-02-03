from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostList, PostDetail, PostViewSet
from .views import UserList, UserDetail, UserViewSet
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
     path('<int:pk>/', PostDetail.as_view()),
     path('', PostList.as_view()),
     #2301
     path('users/', UserList.as_view()),
     path('users/<int:pk>/', UserDetail.as_view()),
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='post')
urlpatterns = router.urls