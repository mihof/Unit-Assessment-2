from django.urls import path
from . import views

urlpatterns = [
  path('', views.switch, name='switch'),
  path('home', views.home, name='home'),
  path('home/<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete')
]