import os
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from urllib.parse import quote

#from core.models import CoreModel as CM

User = get_user_model()

class CoreQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)



class CoreModel(models.Model):
    """ This model has common information thus is used as the
        base class for other models.
        PS: It's fields will be added to those of the child class ;-)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)
    #created_by = models.ForeignKey('auth.User',  on_delete=models.CASCADE)

    objects = CoreQuerySet.as_manager()

    class Meta:
        abstract = True
        ordering = ['created']
