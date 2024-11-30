from django.db import models
from django.db.models import TextField, CharField



def normalize_text(obj: models.Model) -> str:
    """" normalize obj all text fields """
    for field in obj._meta.get_fields():
        if isinstance(field, (TextField, CharField)):
            value = getattr(obj, field.name)
            setattr(obj, field.name, ' '.join(value.split()))