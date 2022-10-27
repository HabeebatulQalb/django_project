from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models,Model):
    first_name = models.Charfield(max_length=400)
    first_name = models.Charfield(max_length=400)
    

class Song(models,Model):
    pass
class lyric(models,Model):