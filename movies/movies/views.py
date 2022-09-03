
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseRedirect

from django.http import JsonResponse
from .serializers import MovieSerializer

""" Mock data 
data = {
    'movies': [
        {
            'id': 5,
            'title': 'Jaws',
            'year': 1998
        },
        {
            'id': 6,
            'title': 'Sharknado',
            'year': 2001
        },
        {
            'id': 7,
            'title': 'The Meg',
            'year': 2010
        }
      
    ]
}
"""
 
def movies(request):
    data = Movie.objects.all()

    # return HttpResponse("Hello there!")
    # return render(request, 'movies/movies.html', data)
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("home page!")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        
        return HttpResponseRedirect("/movies")

    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')

    movie.delete()
    
    return HttpResponseRedirect("/movies")

def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse({"movies": serializer.data}, safe=False)
