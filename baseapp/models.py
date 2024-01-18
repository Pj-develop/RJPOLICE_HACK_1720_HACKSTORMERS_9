from django.db import models

# Create your models here.

# speech_to_text/models.py

from django.db import models

class AudioFile(models.Model):
    file = models.FileField(upload_to='audio_files/')
    transcription = models.TextField()

