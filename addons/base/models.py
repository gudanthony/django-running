
from django.db import models


class TimeStampedModel(models.Model):
    """."""

    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        """."""

        abstract = True
