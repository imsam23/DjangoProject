# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .forms import Student_forms,Login_form

from django.shortcuts import render

# Create your views here.

def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Student_forms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        #form = Student_forms(request.POST)
        form = Student_forms()
    return render(request, 'app_1/index.html', {'form': form})

def welcome(request):
    return render(request,'app_1/welcome.html')

def log_in(request):
    form=Login_form()
    return render(request, 'app_1/log_in.html', {'form': form})



