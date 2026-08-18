from django.urls import path

from accounts.views.delete_view import DeleteUserView
from accounts.views.login_view import LoginView
from accounts.views.logout_view import LogoutView
from accounts.views.profile_view import ProfileView
from accounts.views.register_view import RegisterView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/profile/", ProfileView.as_view(), name="profile"),

    path(
        "users/<int:pk>/delete/",
        DeleteUserView.as_view(),
        name="delete-user",
    ),
]