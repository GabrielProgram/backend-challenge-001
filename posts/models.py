from django.db import models
from helpers.models import TimestampModel, BaseModel, BaseContentModel
from topics.models import Topic


class Post(TimestampModel, BaseModel, BaseContentModel):
    topic = models.ForeignKey(Topic, related_name='topic', on_delete=models.CASCADE)

    class Meta:
        ordering = ['updated_at']
