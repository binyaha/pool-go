from django.urls import re_path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns
from miner import views 

app_name = 'miner'

urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^(?P<miner_id>[0-9]+)/$', views.detail, name = 'detail'),
    re_path(r'^create/$', views.miner_create, name="create"),
    re_path(r'^change', views.change_pool, name='change'),
    # re_path(r'^apipool', views.miner_pool.as_view(), name='api_pool'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)