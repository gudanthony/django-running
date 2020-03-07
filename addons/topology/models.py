
from django.db import models

from author.decorators import with_author
from django_countries.fields import CountryField

from addons.base.models import TimeStampedModel


@with_author
class CountryState(TimeStampedModel):
    """."""

    country = CountryField()
    code = models.CharField('Code', max_length=8, null=True, blank=True)
    name = models.CharField('Country State', max_length=32)
    # image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        """."""
        return self.name

    class Meta:
        """."""

        verbose_name = 'Country State'
        verbose_name_plural = 'Country States'
        ordering = ('name',)


@with_author
class Municipality(TimeStampedModel):
    """."""

    country_state = models.ForeignKey(
        CountryState, on_delete=models.CASCADE,
        related_name='municipalities', related_query_name='municipalities')
    code = models.CharField('Code', max_length=8, null=True, blank=True)
    name = models.CharField('Municipality', max_length=32)
    # image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        """."""
        return self.name

    class Meta:
        """."""

        verbose_name = 'Municipality'
        verbose_name_plural = 'Municipalities'
        ordering = ('name',)


@with_author
class Parish(TimeStampedModel):
    """."""

    municipality = models.ForeignKey(
        Municipality, on_delete=models.CASCADE,
        related_name='parishes', related_query_name='parish')
    code = models.CharField('Code', max_length=8, null=True, blank=True)
    name = models.CharField('Parish', max_length=32)
    # image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        """."""
        return self.name

    class Meta:
        """."""

        verbose_name = 'Parish'
        verbose_name_plural = 'Parishes'
        ordering = ('name',)
