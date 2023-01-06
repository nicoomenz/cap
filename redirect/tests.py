from django.test import TestCase
from django.contrib.auth.models import User
from django.core.cache import cache

from redirect.controller import get_redirect_url, create_historico
from .models import Redirect

class RedirectTests(TestCase):

    def setUp(self) -> None:
        user = User.objects.create_user('tmob', 'tmob@gmail.com', 'tm123456')
        user.save()
        self.client = self.client_class()
        self.client.login(username=user.username, password='tm123456')
        
        self.redirect1 = Redirect.objects.create(key='abcde', url='www.google.com.ar')
    
    def test_get_redirect_url(self):
        url = get_redirect_url(self.redirect1.key)
        self.assertEqual(url, 'www.google.com.ar')
    
    def test_create_historico_not_found(self):
        instance = create_historico(self.redirect1.key)
        self.assertEqual(instance, self.redirect1)
        self.assertEqual(instance.status, 'not_found')

    def test_create_historico_found_db(self):
        instance = create_historico(self.redirect1.key, self.redirect1.url)
        self.assertEqual(instance, self.redirect1)
        self.assertEqual(instance.status, 'db')

    def test_create_historico_not_found_cache(self):
        cache.set('www.google.com.ar', self.redirect1.url)
        instance = create_historico(self.redirect1.key, self.redirect1.url)
        self.assertEqual(instance, self.redirect1)
        self.assertEqual(instance.status, 'cache')