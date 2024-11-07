from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # La ruta raíz debe ir primera
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard con su propia ruta
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación de Django
]