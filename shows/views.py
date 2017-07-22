from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Show
from .forms import ShowForm

# Create your views here.


def show_list(request):
    object_list = Show.objects.all()
    context = {
        'object_list': object_list
    }

    return render(request, 'shows/list.html', context)


def show_create(request):
    if request.method == 'POST':

        form = ShowForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = ShowForm()

    context = {
        'form': form,
    }

    return render(request, 'shows/create.html', context)