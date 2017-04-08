from django.conf.urls import url
from django.contrib import admin

from .views import list_view, detail_view, search_view

urlpatterns = [
    url(r'^$', list_view, name="home" ),
    url(r'^detail/(?P<slug>.+)$', detail_view, name="detail" ),
    url(r'^search', search_view, name='search'),
]