from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50, unique=True)
    like = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ---posted at {self.created_at}'


