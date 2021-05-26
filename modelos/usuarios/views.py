from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import *




def home(request):
    context={'Cliente':Cliente}
    return render(request,'index.html',context)
