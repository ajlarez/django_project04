from django.db import models

# Create your models here.
# creado por yo
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Post Title')
    description = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='static/upload_images', verbose_name='Image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at'] #Ordenar por fecha de creación descendente#