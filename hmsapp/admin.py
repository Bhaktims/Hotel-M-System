from django.contrib import admin
from hmsapp.models import Menu
from hmsapp.models import Bookorder
# Register your models here.

# admin.site.register(Bookorder)
# admin.site.register(Menu)

class BookorderAdmin(admin.ModelAdmin):
    list_display=['id','foodname','qty','cat','name','address','contact']
    list_filter=['foodname','cat'] 

admin.site.register(Bookorder,BookorderAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display=['id','foodname','qty','cat','price','stat']
admin.site.register(Menu,MenuAdmin)

admin.site.site_header="Hotel Management System"
admin.site.site_title="Admin-Hotel Management System"
admin.site.index_title="Admin-Hotel M Sys"