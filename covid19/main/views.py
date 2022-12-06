from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def showData(request):
    data = covid19.objects.all()
    return(render(request, "showdata.html", {"data" : data}))

def addData(request):
    form = CovidDataForm(request.POST)
    if(form.is_valid()):
        form.save()
        return(redirect("/"))
    return(render(request, "adddata.html" , {"form" : form}))
