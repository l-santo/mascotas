from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(
        verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen",
                              upload_to="about", null=True, blank=True)
    author = models.ForeignKey(
        User, verbose_name="Autor", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name="Categorias")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "novedad"
        verbose_name_plural = "novedades"
        ordering = ["-created"]

    def __str__(self):
        return self.title
