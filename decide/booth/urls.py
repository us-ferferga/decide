from django.urls import path
from .views import BoothView, BoothApiView, PingView, NewBoothFrontendView


urlpatterns = [
    path('', NewBoothFrontendView.as_view()),
    path('api', PingView.as_view()),
    path('api/<int:vid>', BoothApiView.as_view()),
    path('new/<int:voting_id>/', NewBoothFrontendView.as_view()),
    path('old/<int:voting_id>/', BoothView.as_view())
]
