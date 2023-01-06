
from .models import HistoricalRedirect, Redirect
from django.core.cache import cache
from django.http import HttpResponseBadRequest
import logging  


def get_url_from_cache(key):
    
    url=cache.get(f'url_keys{key}',None)
    if not url:
        raise ValueError(f'key {key} not found in cache')
    return url


def get_redirect_by_cache(key):
        try:
           url=get_url_from_cache(key)
           create_historico(key,url,status=HistoricalRedirect.CACHE)
           return url 

        except:
            url= get_url_from_db(key)
            create_historico(key,url,status=HistoricalRedirect.DB)
            return url



def get_url_from_db(key):
    try:
        instance=Redirect.objects.get(key=key,active=True)
        return instance.url
    except Redirect.DoesNotExist:
        create_historico(key=key)
        raise ValueError(f'key {key} not found')

def get_redirect_url(key):
        return get_redirect_by_cache(key)

    

def load_redirect_on_cache(redirect,created):
    if not redirect.active:
        return cache.delete(f"url_keys{redirect.key}")
    if created:
        return cache.set(f"url_keys{redirect.key}",redirect.url)
    return cache.set(f"url_keys{redirect.key}",redirect.url)
    
    
def create_historico(key,url=None,status=None):
    try:
        return HistoricalRedirect.create(key,url,status)
    except Exception as e:
        logging.error(f"Error creating historical {e}")
        return HttpResponseBadRequest()