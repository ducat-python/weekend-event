from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Attendee
from shows.models import Show
from .forms import AttendeeForm

# Create your views here.


def register_attendee(request, pk=None):
    if request.method == 'GET':
        pk = request.GET.get('pk')
        show = Show.objects.get(pk=pk)

    if request.method == 'POST':
        pk = request.POST.get('pk')
        show = Show.objects.get(pk=pk)
        form = AttendeeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.show = show
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form = AttendeeForm()

    context = {
        'object': show,
        'form': form
    }

    return render(request, 'attendees/register.html', context)