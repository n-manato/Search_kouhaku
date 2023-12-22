from django.contrib import admin

# Register your models here.
from .models import Parent, League, Year, Participation, Team, Person, Song

admin.site.register(Parent)
admin.site.register(League)
admin.site.register(Year)
admin.site.register(Team)
admin.site.register(Participation)
admin.site.register(Person)
admin.site.register(Song)
