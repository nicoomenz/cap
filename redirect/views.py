from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponseBadRequest
import logging
from .controller import create_historico
from redirect.controller import get_redirect_url
# Create your views here.

@require_GET
def redirect_url(request,key):
    
    try:
        return get_redirect_url(key)

    except Exception as e:
        logging.error(f"Error Try get url {e}")
        return HttpResponseBadRequest()