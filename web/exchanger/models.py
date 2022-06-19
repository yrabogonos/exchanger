from django.db import models

# Create your models here.


class Currency(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sign = models.CharField(max_length=50)
    uah = models.FloatField(blank=False)
    countries = models.CharField(max_length=255)

    def __str__(self):
        return self.name


