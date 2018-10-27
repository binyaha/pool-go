from django.contrib import admin
from .models import Miner, Pool, PoolMux

admin.site.register(Miner)
admin.site.register(Pool)
admin.site.register(PoolMux)
# Register your models here.

