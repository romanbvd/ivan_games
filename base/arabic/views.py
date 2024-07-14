from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Dictionary

def index(request):
    return render(request, "index.html")

def save_word(request):
    Dictionary.objects.create(
        russian=request.POST.get("russian"), 
        arabic=request.POST.get("arabic"),
        transcription=request.POST.get("transcription"),
        )
    
    return HttpResponseRedirect("/")
