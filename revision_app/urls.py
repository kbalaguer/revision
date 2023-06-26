from django.urls import path
from revision_app import views

app_name='revision_app'

urlpatterns = [
    path('', views.inicio, name='inicio'), # el name se usa para poder armar hiper vinculos dentro las htmls
    path('crear', views.crear_gato, name='crear'),          
]
