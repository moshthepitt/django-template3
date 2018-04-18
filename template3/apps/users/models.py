from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel

User = settings.AUTH_USER_MODEL


class UserProfile(TimeStampedModel):

    """
    Model used to store more information on users
    """
    user = models.OneToOneField(User, verbose_name=_("User"),
                                on_delete=models.CASCADE)

    def __str__(self):
        return _("{user}'s profile").format(user=self.user)
