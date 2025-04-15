from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from .models import Cars, CarInventory
from gemini_api.client import get_car_ai_bio

def car_inventory_update():
    cars_count = Cars.objects.count()
    cars_value = Cars.objects.aggregate(total_value=Sum('price'))['total_value'] or 0.00
    CarInventory.objects.create(
        cars_count=cars_count, 
        cars_value=cars_value
    )

    


@receiver(post_save, sender=Cars)
def car_post_save(sender, instance, created, **kwargs):
   if created:
    car_inventory_update()  


@receiver(pre_save, sender=Cars)
def car_pre_save(sender, instance, **kwargs):

    if not instance.bio:
       ai_bio = get_car_ai_bio(
          instance.model, 
          instance.brand.name, 
          instance.year)
       instance.bio = ai_bio


@receiver(pre_delete, sender=Cars)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE ####')


@receiver(post_delete, sender=Cars)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()

