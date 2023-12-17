from django.urls import path
from .views import VisualizerView


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view(), name='visualizer'),
    path('visualizer/<int:voting_id>/graphics/', VisualizerView.graphics, name='graphics'),
]
