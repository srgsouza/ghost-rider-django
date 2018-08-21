from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (Car, Comment, User)

# Register your models here.

# admin.site.register(User, UserAdmin)
admin.site.register(Car)
admin.site.register(Comment)
