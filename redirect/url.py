from django.urls import path
from redirect.views import redirect_url


urlpatterns = [
    path('url/<str:key>', redirect_url, name="redirect"),
]