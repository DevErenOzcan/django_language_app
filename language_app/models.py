from django.db import models
from django.contrib.auth.models import User


class Words(models.Model):
    english = models.CharField(max_length=30)
    turkish = models.CharField(max_length=30)
    img = models.ImageField(upload_to='words_imgs/')


class UserWords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Words, on_delete=models.CASCADE)
    is_learned = models.BooleanField(default=False)
    corect_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'word')