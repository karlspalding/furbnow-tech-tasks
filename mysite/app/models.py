from django.db import models


class Measure(models.Model):
    """
    Energy efficiency measures that could be applied to a property.
    E.g. Loft insulation,
    insulation material deployed in lofts to reduce energy lost through the roof, often 50mm-300mm thick,
    £1000-£2000 for a 3 bed semi-detached house.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.FloatField()
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
