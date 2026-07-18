from django.urls import path

from accounts.views.login_view import LoginView
from accounts.views.profile_view import ProfileView
from accounts.views.register_view import RegisterView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/profile/", ProfileView.as_view(), name="profile"),
]