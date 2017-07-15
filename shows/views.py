from django.shortcuts import render

from .models import Show

# Create your views here.


def show_list(request):
    object_list = Show.objects.all()
    context = {
        'object_list': object_list
    }

    return render(request, 'shows/list.html', context)