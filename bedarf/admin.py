from django.contrib import admin
from .models import Bedarf

# Register your models here.


class BedarfModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Bedarf, BedarfModelAdmin)
