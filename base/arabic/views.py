from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from arabic.models import Word

def index(request):
    wordsQuerySet = Word.objects.all()

    return render(request, "index.html", {'words_list': wordsQuerySet})

