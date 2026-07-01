from django.urls import path
from .views import VillageListCreateView, VillageDetailView
from .views import CensusAutoFillView
from .views import VillageBoundaryView

urlpatterns = [
    path('villages/', VillageListCreateView.as_view()),
    path('villages/<int:pk>/', VillageDetailView.as_view()),
    path('census/autofill/', CensusAutoFillView.as_view()),
    path('villages/boundary/', VillageBoundaryView.as_view()),
]