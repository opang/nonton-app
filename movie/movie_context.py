from .models import Movie

def slider_movies(request):
    movies = Movie.objects.filter(status= 'TR')[0:1]
    #movies = Movie.objects.last()
    return {'slider_movies' : movies}