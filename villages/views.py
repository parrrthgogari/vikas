from rest_framework import generics
from .models import Village, SubDistrictCensus
from .serializers import VillageSerializer
from rest_framework.views import APIView, Response
import requests

class VillageListCreateView(generics.ListCreateAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

class VillageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

class CensusAutoFillView(APIView):
    def get(self, request):
        name = request.query_params.get('name', '')
        if not name:
            return Response({"error": "name parameter required"}, status=400)
        
        result = SubDistrictCensus.objects.filter(
            name__icontains=name
        ).first()
        
        if not result:
            return Response({"error": "No data found"}, status=404)
        
        return Response({
            "name": result.name,
            "population_2011": result.population_2011,
            "males": result.males,
            "females": result.females,
            "area_sqkm": result.area_sqkm,
            "district_code": result.district_code,
        })

class VillageBoundaryView(APIView):
    def get(self, request):
        name = request.query_params.get('name', '')
        if not name:
            return Response({"error": "name parameter required"}, status=400)

        query = f"""
        [out:json][timeout:30];
        area["name"="Maharashtra"]["admin_level"="4"]->.searchArea;
        relation["boundary"="administrative"]["name"="{name}"](area.searchArea);
        out geom;
        """
        try:
            res = requests.post(
                "https://overpass-api.de/api/interpreter",
                data={"data": query},
                headers={"User-Agent": "VIKAS/1.0 (vikas-gp-tool@gmail.com)"},

                timeout=25
            )
            print("STATUS:", res.status_code)
            print("RESPONSE:", res.text[:500])
            
            data = res.json()
            if not data.get("elements"):
                return Response({"error": "No boundary found"}, status=404)
            return Response(data)
        except Exception as e:
            print("ERROR:", str(e))
            return Response({"error": str(e)}, status=500)