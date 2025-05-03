from django.urls import path, include
from .views import SignUpView,home # importamos la vista de registro de usuarios

urlpatterns = [
    path("/auth", include("django.contrib.auth.urls")), # urls de autenticacion de django
    path('signup/', SignUpView.as_view(), name='signup'), # url para el registro de usuarios
    path('', home, name='home'), # url para la pagina de inicio

]