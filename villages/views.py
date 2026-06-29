from rest_framework import generics
from .models import Village
from .serializers import VillageSerializer

class VillageListCreateView(generics.ListCreateAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

class VillageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer