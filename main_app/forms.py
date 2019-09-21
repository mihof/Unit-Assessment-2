from django import forms
from .models import Wacky_Widgets

class WidgetForm(forms.ModelForm):
  class Meta:
    model = Wacky_Widgets
    fields = '__all__'