from django.db import models

class FlashcardSet(models.Model):
    name = models.CharField(max_length=200)
    creator = models.CharField(max_length=40)
    password = models.CharField(max_length=60)
    description = models.CharField(max_length=1000)
    identifier = models.CharField(max_length=40, unique=True)
    
    
class Flashcard(models.Model):
    flashcardset = models.ForeignKey(FlashcardSet, on_delete=models.CASCADE)
    value_a = models.CharField(max_length=1000)
    value_b = models.CharField(max_length=1000)
    identifier = models.CharField(max_length=40, unique=True)

