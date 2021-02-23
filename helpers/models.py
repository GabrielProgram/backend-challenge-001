"""
Model helper
"""
###
# Libraries
###
from django.db import models
from accounts.models import User


###
# Helpers
###
class TimestampModel(models.Model):
    '''
        Extend this model if you wish to have automatically updated
        created_at and updated_at fields.
    '''

    class Meta:
        abstract = True

    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class BaseContentModel(models.Model):
    class Meta:
        abstract = True

    content = models.TextField(blank=False)
