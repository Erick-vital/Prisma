from django.forms import ModelForm
from .models import Contanto

class ContactoForm(ModelForm):
    class Meta:
        model = Contanto
        fields = '__all__'