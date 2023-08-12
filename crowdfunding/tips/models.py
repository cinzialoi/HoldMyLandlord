from django.db import models
from django.contrib.auth import get_user_model

class Tip(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    pheasant= models.CharField(max_length=200)
    landlord = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
        related_name='tips'
    )

