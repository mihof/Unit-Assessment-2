from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from .models import Wacky_Widgets
from .forms import WidgetForm

# Create your views here.
def switch(request):
  return redirect('home')

def home(request):
  widgets = Wacky_Widgets.objects.all()
  form = WidgetForm
  if request.method == 'POST':
    new_form = WidgetForm(request.POST)
    if new_form.is_valid():
      new_form.save()
      return redirect('home')
    else:
      pass
  return render(request, 'home.html', { 'widgets': widgets, 'form': form })

class WidgetDelete(DeleteView):
  model = Wacky_Widgets
  success_url = '/home'


 