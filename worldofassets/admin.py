from django.contrib import admin
from .models import *

admin.site.register(Asset)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Game)
admin.site.register(Category)

