from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView #yo
from django.views.generic import DeleteView #yo
from .models import Post #yo 
from django.views.generic import ListView, DetailView #yo

from django.urls import reverse_lazy #yo
# Create your views here.

class PostListView(ListView):
        template_name = 'post_list.html'
        model= Post
        context_object_name = 'lista_de_objects' #cambia el nombre de la lista de objetos

class PostCreate(CreateView):

        template_name = 'post_create.html'
        model= Post 
        fields = ["title", "description", "image"]
        #fields = '__all__' para poner todos los campos del modelo
        success_url=reverse_lazy("post_list") #redirecciona a la url que se le indique, en este caso a la raiz del proyecto

class PostRead(DetailView):
        template_name = 'post_detail.html'
        model= Post
        context_object_name = 'post' #cambia el nombre de la lista de objetos

class PostUpdate(UpdateView):
        template_name = "post_update.html"
        model = Post
        success_url=reverse_lazy("post_list") #redirecciona a la url que se le indique, en este caso a la raiz del proyecto
        fields = [ "title", "description", "image"]
        #fields = '__all__' para poner todos los campos del modelo

class PostDelete(DeleteView):
        template_name = "post_delete.html"
        model = Post
        success_url=reverse_lazy("post_list")



