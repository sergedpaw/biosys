from django.contrib import admin
from django.http import HttpResponse
from models import MyModel


def export_template(modeladmin, request, queryset):
    pass

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    pass

