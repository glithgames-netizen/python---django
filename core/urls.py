from django.urls import path
from . import views

urlpatterns = [
    # Esta linha conecta o caminho (que vem do projeto principal) com a sua view 'home'
    path('', views.home, name='home'),]