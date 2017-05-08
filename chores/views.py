from django.shortcuts import render
from django.http import HttpResponse

from .forms import ChoreForm


def index(request):
    form = ChoreForm()
    return render(request, 'chores/index.html', {'form': form})
