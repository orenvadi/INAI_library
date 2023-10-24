from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("create/category/", CategoriesCreateAPIView.as_view()),
    path("list/category/", CategoriesListAPIView.as_view()),
    path("change/category/<int:pk>/", CategoriesChangeAPIView.as_view()),
    path("create/book/", BooksCreateAPIView.as_view()),
    path("list/book/", BooksListAPIView.as_view()),
    path("change/book/<int:pk>/", BooksChangeAPIView.as_view()),
]
