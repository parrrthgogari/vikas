from django.urls import path
from .views import VillageListCreateView, VillageDetailView

urlpatterns = [
    path('villages/', VillageListCreateView.as_view()),
    path('villages/<int:pk>/', VillageDetailView.as_view()),
]