from django.contrib import admin
from arabic.models import Word
from django.db import models

class WordAdmin(admin.ModelAdmin):
    list_display = ('arabic', 'russian', 'transcription', 'examples')
    formfield_overrides = {
        models.CharField: {'required': False},
    }

admin.site.register(Word, WordAdmin)