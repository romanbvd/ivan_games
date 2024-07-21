from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import Dictionary

def index(request, id=0):
    wordsQuerySet = Dictionary.objects.all()
    
    context = {'words_list': wordsQuerySet}
    if id:
        context['word'] = Dictionary.objects.get(id=id)

    return render(request, "edit.html", context=context)

def add_word(request):
    if request.method == "POST":
        Dictionary.objects.create(
            russian=request.POST.get("russian"), 
            arabic=request.POST.get("arabic"),
            transcription=request.POST.get("transcription"),
            )
    
    return HttpResponseRedirect("/")

def edit_word(request, id):
    try:
        word = Dictionary.objects.get(id=id)
        wordsQuerySet = Dictionary.objects.all()

        if request.method == "POST":
            word.russian = request.POST.get("russian")
            word.arabic=request.POST.get("arabic")
            word.transcription=request.POST.get("transcription")
            word.save()

            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"word": word, 'words_list': wordsQuerySet})
    except Dictionary.DoesNotExist:
        return HttpResponseNotFound("<h2>Word not found</h2>")

    return HttpResponseRedirect("/")

def delete_word(request, id):
    try:
        word = Dictionary.objects.get(id=id)
        word.delete()
        
        return HttpResponseRedirect("/")
    except Dictionary.DoesNotExist:
        return HttpResponseNotFound("<h2>Word not found</h2>")
