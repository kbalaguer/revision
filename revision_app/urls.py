from django.urls import path
from revision_app import views

app_name='revision_app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear', views.crear_gato, name='crear'),          
]
