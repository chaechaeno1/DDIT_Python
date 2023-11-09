from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



def mem_list(request):
    return render(request, 'mem_list.html')







