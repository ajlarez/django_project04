from django.shortcuts import render
from django.views.generic import CreateView # creado para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm # formulario de registro de usuarios
from django.urls import reverse_lazy # para redirigir a la pagina de login
# Create your views here.
class SignUpView(CreateView):
    template_name = 'authentication/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list') # redirige a la pagina de inicio de sesion

    """ def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)"""	