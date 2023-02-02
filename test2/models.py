from django.db import models
from test1.models import Post

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    def __str__(self):
        return f'{self.comment} --- {self.post}'