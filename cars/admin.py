from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class  CarAdmin(admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src= "{}" width = "40" style="border_radius:100px"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'photo'
    list_display = ('id','thumbnail','car_title','state','color','model','body_style','fuel_type','is_featured')
    list_display_links = ('id','thumbnail','car_title')
    search_fields = ('id','car_title','body_style','fuel_type')
    list_filter = ('model','fuel_type','body_style')
    list_editable = ('is_featured',)



admin.site.register(Car,CarAdmin)
