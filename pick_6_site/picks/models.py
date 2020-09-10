from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
from django.db.models import CharField


class Pick(models.Model):
    pick_text = models.CharField(max_length=40)
    pick_type = models.CharField(max_length=40)
    pts = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published', default=True)

    def __str__(self):
        return self.pick_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# pick_text: CharField = models.CharField(max_length=40)
# pick_type = models.CharField(max_length=40)
# pts = models.CharField(max_length=40)
# Pick_date = models.DateTimeField('date published')
