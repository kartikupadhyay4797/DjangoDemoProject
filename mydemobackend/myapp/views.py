from django.shortcuts import render

from django.http import HttpResponse
def fn1(request):
    return HttpResponse("<h>HomePage of MyApp</h>")