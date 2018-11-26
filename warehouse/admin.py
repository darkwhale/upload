from django.contrib import admin

# Register your models here.

from warehouse import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'password', 'grade')


admin.site.register(models.User, UserAdmin)
