from __future__ import unicode_literals

from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    category = models.CharField(max_length=50, default='General')
    email = models.CharField(max_length=150)
    comment = models.CharField(max_length=1000)
    has_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'feedback'

