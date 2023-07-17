
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('This is the home page!')

def movies(request):
    return render(request, 'movies/movies.html', {'movies': ['movie1', 'movie2', 'movie3']})