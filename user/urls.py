from django.urls import path, include
from .views import (RegisterView,LoginView, UserProfileView, LogoutView, VerifyEmailView,
                   PasswordResetRequestView, PasswordResetConfirmView,
                   ChangePasswordView, SocialLoginSuccess)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Your custom auth endpoints
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/v1/profile/', UserProfileView.as_view(), name='user_profile'),
    path('api/v1/logout/', LogoutView.as_view(), name='logout'),
    path("api/v1/verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path("api/v1/password-reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path('api/v1/password-reset/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('api/v1/change-password/', ChangePasswordView.as_view(), name='change-password'),


    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),

    # allauth endpoints
    path("api/v1/auth/", include("allauth.urls")),
    path("api/v1/auth/social/", include("allauth.socialaccount.urls")),

    # Social login success view
    path("/auth/social/login/success/", SocialLoginSuccess.as_view(), name="social"),



]