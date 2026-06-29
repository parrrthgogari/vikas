import csv
import os
from django.core.management.base import BaseCommand
from villages.models import SubDistrictCensus

class Command(BaseCommand):
    help = 'Load Maharashtra census data from CSV'

    def handle(self, *args, **kwargs):
        csv_path = os.path.join('villages', 'data', 'maharashtra_census.csv')

        SubDistrictCensus.objects.all().delete()  # fresh load

        count = 0
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                SubDistrictCensus.objects.create(
                    district_code=row['district_code'],
                    subdistrict_code=row['subdistrict_code'],
                    name=row['name'],
                    population_2011=int(float(row['population_2011'])),
                    males=int(float(row['males'])),
                    females=int(float(row['females'])),
                    area_sqkm=float(row['area_sqkm']) if row['area_sqkm'] else None,
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Loaded {count} sub-districts into Supabase'))