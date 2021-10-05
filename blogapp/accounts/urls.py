from django.urls import path, include
from accounts.views import ChangePasswordView
urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls')),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]