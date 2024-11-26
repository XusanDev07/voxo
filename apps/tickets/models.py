from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models.base_model import AbstractBaseModel
from django.conf import settings


class Ticket(AbstractBaseModel):
    class Status(models.TextChoices):
        NEW = 'NEW', _('New')
        IN_PROGRESS = 'IN_PROGRESS', _('In progress')
        RESOLVED = 'RESOLVED', _('Resolved')
        CLOSED = 'CLOSED', _('Closed')

    class Priority(models.TextChoices):
        LOW = 'LOW', _('Low')
        MEDIUM = 'MEDIUM', _('Medium')
        HIGH = 'HIGH', _('High')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.CharField(
        max_length=50,
        choices=Status.choices,
        default=Status.NEW
    )
    priority = models.CharField(
        max_length=50,
        choices=Priority.choices,
        default=Priority.HIGH
    )
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Support Ticket'
        verbose_name_plural = 'Support Tickets'
        ordering = ['-created_at']