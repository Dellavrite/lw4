from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Film
from .forms import FilmForm

# Create your views here.
def create_film(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('')

    form = FilmForm

    if request.method == 'POST':
        form = FilmForm(request.POST)
        
        if not form.is_valid():
            return render(request, 'form.html', context={'form': form})

        model = Film.objects.create(
            name = form.cleaned_data['name'],
            categorys = form.cleaned_data['categorys'],
            date_post = form.cleaned_data['date_post'],
            actors = form.cleaned_data['actors'],
            date_view = form.cleaned_data['date_view'],
        )
        model.save()

    return render(request, 'form.html', context={'form': form})

def view_film(request):
    return render(request, 'index.html', context={"films": Film.objects.all()})

def edit_film(request, pk=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('')

    form = FilmForm

    if request.method == 'POST':
        form = FilmForm(request.POST)
        
        if not form.is_valid():
            return render(request, 'form.html', context={'form': form})

        Film.objects.filter(pk=pk).update(
            name = form.cleaned_data['name'],
            categorys = form.cleaned_data['categorys'],
            date_post = form.cleaned_data['date_post'],
            actors = form.cleaned_data['actors'],
            date_view = form.cleaned_data['date_view'],
        )
    return render(request, 'form.html', context={'form': form})


def delete_film(request, pk=0):
    Film.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('http://localhost:8000/')