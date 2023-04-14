from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Rating, Reviews, Actor, RatingStar

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Actor)
admin.site.register(RatingStar)

