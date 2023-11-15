from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .views import GetUserView, LogoutView, RegisterView, account, ObtainSocialAuthTokenView


urlpatterns = [
    path('login/', obtain_auth_token),
    path('login-social/', ObtainSocialAuthTokenView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterView.as_view()),
    ]
