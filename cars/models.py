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
    picture = models.ImageField(upload_to='cars/cars_photo', blank=True, null=True, default='cars/cars_photo/default.jpg')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
    


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:#Ordenar por data de criação de forma decrescente
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'