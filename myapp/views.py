from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def sayHello(response):
	return HttpResponse('hello')

def hello2(response, username):
	return HttpResponse('Are you ok? I am fine '+ username)

def hello3(request, username):
	now = datetime.now()
	return render(request, "hello3.html", locals())


def hello4(request, username):
	now = datetime.now()
	return render(request, "hello4.html", locals())