from django.urls import path

from .views import (GroupChangeAPIView, GroupCreateAPIView, UserGetAPIView,
                    UserListAPIView, UserLoginAPIView, UserLogoutAPIView,
                    UserRegisterAPIView)

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view()),
    path("login/", UserLoginAPIView.as_view()),
    path("logout/", UserLogoutAPIView.as_view()),
    path("get/user/", UserGetAPIView.as_view()),
    path("list/user/", UserListAPIView.as_view()),
    path("create/group/", GroupCreateAPIView.as_view()),
    path("change/group/", GroupChangeAPIView.as_view()),
]
