from django.contrib.auth.models import User
from django.db import models


class TimeEntry(models.Model):
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.description