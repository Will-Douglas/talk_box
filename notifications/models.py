from django.db import models

from nu_talker.models import NuTalker
# from posts.models import TalkTalk

# Create your models here.
class Notify(models.Model):
    speaker = models.ForeignKey(NuTalker, on_delete=models.CASCADE)
    # statement = models.ForeignKey(TalkTalk, on_delete=models.CASCADE)
    check_notify = models.BooleanField(default=False)
