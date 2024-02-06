from django.contrib import admin

# Register your models here.

from app1.models import Place

from app1.models import Team

admin.site.register(Place)
admin.site.register(Team)
