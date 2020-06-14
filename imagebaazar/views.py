from django.shortcuts import render

from django.http import HttpResponse
from myapp.models import *

def show(request):

    return render(request, "about.html")



def homey(request):
    images=Image.objects.all()
    cats=Category.objects.all()
    data={'images':images,'cats':cats}
    return render(request,"home.html",data)

def showcat(request,cid):
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)


def index(request):
    return render(request,"re.html")
