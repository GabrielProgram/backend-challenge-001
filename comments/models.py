from django.db import models
from helpers.models import BaseContentModel, TimestampModel, BaseModel
from posts.models import Post


class Comment(TimestampModel, BaseModel, BaseContentModel):
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
