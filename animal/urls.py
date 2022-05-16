from django.urls import path

from animal import views

app_name = 'animal'

urlpatterns = [
    path('panda/', views.panda, name='panda'),
    path('cat/', views.cat, name='cat'),
]