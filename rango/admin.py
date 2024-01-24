from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

class PageAdmin (admin.ModelsAdmin):
    list_display = ('title', 'catagory', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
