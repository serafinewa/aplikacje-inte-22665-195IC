from django.urls import path

from api.views import BookDetail
from .views import BookListView


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('<int:pk>/', BookDetail.as_view()),
]
