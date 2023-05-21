from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    data = {
        'tittle': 'home page',
        
        'trial': 'He watched as the young man tried to impress everyone in the room with his intelligence. There was no doubt that he was smart. The fact that he was more intelligent than anyone else in the room could have been easily deduced, but nobody was really paying any attention due to the fact that it was also obvious that the young man only cared about his intelligence.',
        
        'list': ['young man', ' obvious', 'fun', 'gift'],
        
        'contact': [
            {'name': 'aman', 'class': '11'},
            {'name': 'rohit', 'class': '12'}
        ],
        
        'numbers': [22, 44, 35, 46, 86]
    }
    return render(request, "base/home.html", data)

def helloworld(request):
    return HttpResponse("hello world")

def innerhello(request, helloid):

    return HttpResponse(helloid)

def allhello(request, allid):
    return HttpResponse(allid)

def aboutus(request):
    return render(request, "base/about.html")

def services(request):
    return render(request, "base/services.html")