from django.shortcuts import render, redirect
from django.db.models import Q
from cars.models import Cars
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView


class CarsView(View):

    def get(self, request):
        search = request.GET.get('search')   
        cars = Cars.objects.all().order_by('model')

        if search:
            cars = cars.filter(Q(model__icontains=search) | Q(brand__name__icontains=search))#Uso de Q objects: Isso permite combinar múltiplas condições de filtragem em uma única consulta, melhorando a legibilidade e a eficiência.
        return render(
            request,
                    'cars.html',
                    {'cars': cars})



class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render (request, 'new_car.html', {'new_car_form': new_car_form})