from django.db import models
from django.utils import timezone
from django.db.models.fields.related import ForeignKey
from nu_talker.models import NuTalker


# Create your models here.

class TalkTalk(models.Model):
    body = models.TextField(max_length=300)
    talk_stated = models.DateTimeField(default=timezone.now)
    spokesmen = models.ForeignKey(NuTalker, on_delete=models.CASCADE)