from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Album(models.Model):

    name = models.TextField()
    artist = models.TextField()
    release_date = models.DateField(default="2024-02-28")
    genre = models.TextField()
    spotify_id = models.CharField(max_length=22)  # length of spotify id

    def __str__(self):
        return f'{self.name} by {self.artist}'
        # return str(self.id)


class Review(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})


class Comment(models.Model):

    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})
