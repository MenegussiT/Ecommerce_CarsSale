from django import forms
from cars.models import Brand, Cars


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

#Criando validações personalizadas    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 20000:
            self.add_error('price', 'O valor não pode ser menor do que R$: 20000')
        return price    

