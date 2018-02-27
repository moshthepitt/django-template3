from django.db import models


class CoreManager(models.Manager):

    use_for_related_fields = True

    def get_queryset(self):
        return super(CoreManager, self).get_queryset()

    def active(self):
        return self.get_queryset().filter(active=True).distinct()
