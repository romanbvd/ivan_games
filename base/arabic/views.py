from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseNotFound

from arabic.models import Word

def index(request):
    words = Word.objects.all()
    paginator = Paginator(words, 20)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {'page_obj': page_obj})

