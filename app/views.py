from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun(request):
    return HttpResponse('DATA IS CREATED')
def pavan(request):
    return HttpResponse('<h1> pavan is a python student</h1>')
def harshad(request):
    return HttpResponse('<h1><marquee> harshad sir is a python trainer<h1></marquee>')
def jani(request):
    return HttpResponse('<img src=https://tse1.mm.bing.net/th?id=OIP.siZ58GCWsyWbSzHpRywPgwHaFj&pid=Api</img src>')