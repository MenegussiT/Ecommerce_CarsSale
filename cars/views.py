from django.shortcuts import render, redirect
from django.db.models import Q
from cars.models import Cars
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView


class CarsView(ListView):
    model = Cars
    template_name = 'cars.html'
    context_object_name = 'cars'
    def get_queryset(self):
        cars_query = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars_query = cars_query.filter(model__icontains=search)
        return cars_query


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