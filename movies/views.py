
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'movies': ['Designated Survivor', 'London Has Fallen', 'Avator']})

def movies(request):
    return render(request, 'movies/movies.html', {'movies': ['movie1', 'movie2', 'movie3']})