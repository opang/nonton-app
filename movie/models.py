from django.db import models
from django.utils.text import slugify
from django.utils import timezone
CATEGORY_CHOICES = (
    ('action' , 'ACTION'),
    ('drama' , 'DRAMA'),
    ('comedy' , 'COMEDY'),
    ('romance' , 'ROMANCE'),
    ('horror' , 'HORROR'),
    ('thriller' , 'THRILLER'),
    ('animation' , 'ANIMATION'),
    ('advanture' , 'ADVANTURE'),
    
)

STATUS_CHOICES = (
    ('MW' , 'MOST WATCHED'),
    ('MT' , 'MOST WATCHED2'),
    ('MR' , 'MOST WATCHED3'),
    ('TR' , 'TOP RATED'),
    ('TT' , 'TOP RATED2'),
    ('FT' , 'FEATURED MOV'),

)

# Create your models here.
class Movie(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year = models.DateField()
    cast = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Movie , self).save(*args, **kwargs)


    def __str__(self):
        return self.title



LINK_CHOICES = (
    ('D' , 'DOWNLOAD LINK'),
    ('W' , 'WATCH LINK'),
)

class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __int__(self):
        return self.movie