from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.utils.models.base_model import AbstractBaseModel


class Region(AbstractBaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def clean(self):
        self.name = slugify(self.name)
        if Region.objects.exclude(pk=self.pk).filter(self=self.slug).exists():
            raise ValidationError("{name} already exists ".format(name=self.name))

    class Meta:
        db_table = 'regions'
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')
        ordering = ['name']
