from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

from redirect.controller import load_redirect_on_cache

from .models import Redirect


@receiver(post_save, sender=Redirect)
def cache_wrap_config_reload(sender, instance, created, **kwargs):
    logging.debug('Reload Redirect on cache')
    load_redirect_on_cache(instance,created)