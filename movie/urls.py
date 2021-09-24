from django.urls import path
from.views import MovieList, MovieDetail ,MovieCategory, MovieSearch

app_name = 'movie'



urlpatterns = [
    path('', MovieList.as_view() , name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view() , name='movie_category'),
    path('search/', MovieSearch.as_view() , name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view() , name='movie_detail'),
]

