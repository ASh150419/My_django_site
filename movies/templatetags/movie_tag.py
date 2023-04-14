from django import template
from movies.models import Movie


register = template.Library()

@register.inclusion_tag('movies/tags/last_add_movie.html')
def get_last_add_movie():
    """Вывод последних добавленных фильмов"""
    movies = Movie.objects.order_by("id")[:6]
    return {"last_add_movie": movies}