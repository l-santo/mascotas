from django.shortcuts import render
from .models import Gallery
# Create your views here.


def gallery(request):
     gallerys = Gallery.objects.all()
     return render(request,"gallery/gallery.html",{'gallerys':gallerys})
