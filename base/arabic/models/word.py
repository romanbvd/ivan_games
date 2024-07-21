from django.db import models

class Word(models.Model):
    arabic = models.CharField(max_length=100)
    russian = models.CharField(max_length=100)
    transcription = models.CharField(max_length=100, null=True)
    examples = models.CharField(max_length=250, null=True)
    created_at=models.DateTimeField(auto_now=True)
