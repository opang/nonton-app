from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views.generic import ListView , DetailView
from.models import Movie ,MovieLinks






class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'



    def get_context_data(self, **kwargs):
        context = super(HomeView , self).get_context_data(**kwargs)
        context ['top_rated'] = Movie.objects.filter(status= 'TR')
        context ['top_rated2'] = Movie.objects.filter(status= 'TT')
        context ['most_watched'] = Movie.objects.filter(status= 'MW')
        context ['most_watched2'] = Movie.objects.filter(status= 'MT')
        context ['most_watched3'] = Movie.objects.filter(status= 'MR')
        return context


class MovieList(ListView):
    model = Movie
    paginate_by = 10



class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail , self).get_object()
        return object
    
    def get_context_data(self, **kwargs):
        context = super(MovieDetail , self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)#.order_by['created'][0:6]
        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by = 8
    
    


    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory , self).get_context_data(**kwargs)
        context ['movie_category'] = self.category
        return context


class MovieSearch(ListView):
    model = Movie
    paginate_by = 8
    
 
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list  = self.model.objects.filter(title__icontains=query)
        else:
            pass
        
        return object_list

        

        

    


    
   
       