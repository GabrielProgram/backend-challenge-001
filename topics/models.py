from django.db import models

from helpers.models import TimestampModel, BaseModel


class Topic(TimestampModel, BaseModel):
    urlname = models.SlugField(blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    class Meta:
        ordering = ['updated_at']
