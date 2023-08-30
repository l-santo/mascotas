from django.db import models

# Create your models here.


class Gallery(models.Model):
    title1 = models.CharField(max_length=200, verbose_name="Título")
    image = models.ImageField(verbose_name="Imagen", upload_to="gallerys")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes"
        ordering = ["created"]

    def __str__(self):
        return self.title1
