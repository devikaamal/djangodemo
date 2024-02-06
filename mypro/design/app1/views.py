from django.shortcuts import render

from app1.models import Place

from app1.models import Team


# Create your views here.


def home(request):
    p = Place.objects.all()
    t = Team.objects.all()
    return render(request, 'home.html', {'p': p, 't': t})
