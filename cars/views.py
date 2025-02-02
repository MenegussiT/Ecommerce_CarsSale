from django.shortcuts import render, redirect
from django.db.models import Q
from cars.models import Cars
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


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


class NewCarView(CreateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'

class CarDatailView(DetailView):
    model = Cars
    template_name = 'car_detail.html'
    

class CarUpdateView(UpdateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'car_update.html'
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk':self.object.ok})

class CarDeleteView(DeleteView):
    model = Cars
    template_name = 'car_delete.html'
    success_url = '/cars/'