import os
import uuid

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def clipdir(_, filename):
    _, ext = os.path.splitext(filename)
    return f"clips/{uuid.uuid4().hex}{ext}"


class Clip(models.Model):
    name = models.CharField(
        _("name"),
        max_length=256,
        validators=[MinLengthValidator(1)],
    )
    ident = models.CharField(
        _("ident"),
        max_length=256,
        validators=[MinLengthValidator(1)],
        unique=True,
    )
    keywords = models.TextField(_("keywords"))
    file = models.FileField(_("file"), upload_to=clipdir)

    is_active = models.BooleanField(_("active"), default=False)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("clip")
        verbose_name_plural = _("clips")
        indexes = [models.Index(fields=["is_active"])]
