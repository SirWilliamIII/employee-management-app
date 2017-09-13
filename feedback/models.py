from __future__ import unicode_literals

from django.db import models

from django.core.validators import EmailValidator, MinLengthValidator


class Feedback(models.Model):

    CATEGORY_CHOICES = (
        ('1', 'General'),
        ('2', 'Management'),
        ('3', 'Compensation'),
        ('4', 'Suggestions'),
        ('5', 'Complaint'),
    )

    name = models.CharField(max_length=100)
    emp_no = models.IntegerField()
    subject = models.CharField(max_length=250)
    category = models.CharField(max_length=50, default='1', choices=CATEGORY_CHOICES)
    email = models.CharField(max_length=150, validators=[EmailValidator(), MinLengthValidator(7)])
    comment = models.CharField(max_length=1000)
    has_read = models.BooleanField(default=False)
    created_on = models.DateField(null=False)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'feedback'
