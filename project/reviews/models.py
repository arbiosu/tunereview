from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

