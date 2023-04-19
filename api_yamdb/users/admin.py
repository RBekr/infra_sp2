from django.conf import settings
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'bio', 'role')
    search_fields = ('username',)
    list_filter = ('id',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY
