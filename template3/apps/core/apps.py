from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'template3.apps.core'

    def ready(self):
        import template3.apps.users.signals  # noqa
