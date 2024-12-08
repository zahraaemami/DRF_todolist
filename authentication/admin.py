from django.contrib import admin

# Register your models here.

from .models import user ,UserAdmin

class UserAdmin(admin.UserAdmin) :
    list_display = ('username',)
    search-fields = ('username',)

admin.site.regester(User, userAdmin)