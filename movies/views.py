from django.http import HttpResponse
from django.shortcuts import render

data = {'movies': [

    {
        'id': 5,
        'title': 'Jaws',
        'year': 1987,
    },
    {
        'id': 6,
        'title': 'The Burial',
        'year': 2023,
    },
    {
        'id': 7,
        'title': 'The Departed',
        'year': 2006,
    }
                   
                   ]}

def movies(request):
    return render(request, 'movies/movies.html', data ) 

def home(request):
    return HttpResponse("home")