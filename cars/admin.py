from django.contrib import admin
from cars.models import Cars, Brand

class CarsAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'price', 'color', 'brand')
    search_fields = ('model', 'year', 'price', 'color', 'brand')
    list_filter = ('model', 'year', 'price', 'color', 'brand',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Cars, CarsAdmin)
admin.site.register(Brand, BrandAdmin)