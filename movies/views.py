from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Movie, Genre, Category
from django.views.generic.base import View
from .forms import ReviewForm, RatingForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class GenreYear:
    """Жанры и год выхода фильма"""
    
    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")
    

class MovieView(GenreYear, ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    paginate_by = 3

class MovieDetailView(LoginRequiredMixin, GenreYear, DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"


    
class AddReview(LoginRequiredMixin, GenreYear, View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
    

class FilterMovie(GenreYear, ListView):
    """Фильтр фильмов"""
    paginate_by = 3
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context
    

class Search(ListView):
    """Поиск фильмов"""
    paginate_by = 1

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("search"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search"] = f'search={self.request.GET.get("search")}&'
        return context 
