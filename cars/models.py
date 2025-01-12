from django.db import models

# Create your models here.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    picture = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.model
    


