from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)


class Words(models.Model):
    english = models.CharField(max_length=30)
    turkish = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/')


class UserWords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Words, on_delete=models.CASCADE)
    is_learned = models.BooleanField(default=False)
    corect_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'word')