from django.urls import path
from .views import VisualizerView
from . import views


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view()),
    path('visualizer/<int:voting_id>/graphics/', views.graphics),
]
