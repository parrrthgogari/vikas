from django.db import models


class Village(models.Model):
    name = models.CharField(max_length=200)
    pincode = models.CharField(max_length=10)
    population = models.IntegerField()
    growth_rate = models.FloatField(help_text="Annual % growth rate")
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SubDistrictCensus(models.Model):
    district_code = models.CharField(max_length=10)
    subdistrict_code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    population_2011 = models.IntegerField()
    males = models.IntegerField()
    females = models.IntegerField()
    area_sqkm = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub-District Census Data"