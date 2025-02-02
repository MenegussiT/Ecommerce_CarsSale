from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Cars

@receiver(post_save, sender=Cars)
def car_post_save(sender, instance, created, **kwargs):
    print('### POST SAVE ####')

@receiver(pre_save, sender=Cars)
def car_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE ####')

@receiver(pre_delete, sender=Cars)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE ####')

@receiver(post_delete, sender=Cars)
def car_post_delete(sender, instance, **kwargs):
    print('### POST DELETE ####')