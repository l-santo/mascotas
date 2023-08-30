from django.shortcuts import render, get_object_or_404
from .models import About, Category
# Create your views here.

def about(request):
    abouts = About.objects.all()
    return render(request,"about/about.html",{'abouts':abouts})

def category(request, categoryId):
    #category=Category.objects.get(id=categoryId)
    catego=get_object_or_404(Category, id=categoryId)
    # filtar las entradas de acuerdo a la categia
    abouts=About.objects.filter(category=catego)
    return render(request ,"about/category.html",{"abouts":abouts})