from django.urls import path
from accounts.views.reset_password_view import ResetPasswordView
from accounts.views.logout_view import LogoutView
from accounts.views.login_view import LoginView
from accounts.views.profile_view import ProfileView
from accounts.views.register_view import RegisterView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/profile/", ProfileView.as_view(), name="profile"),
    path(
    "auth/logout/",
    LogoutView.as_view(),
    name="logout",
),
    path(
    "auth/reset-password/",
    ResetPasswordView.as_view(),
    name="reset-password",
),
]