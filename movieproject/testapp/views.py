from django.shortcuts import render
from testapp.models import Movie
from testapp import forms
def index_form(request):
    return render(request,"testapp/movie.html")
def movie(request):
    form=forms.MovieForm()
    if request.method=="POST":
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return index_form(request)
    return render(request,"testapp/movie1.html",{"form":form})
def list_movie(request):
    m1=Movie.objects.all()
    return render(request,"testapp/movie2.html",{"m1":m1})
