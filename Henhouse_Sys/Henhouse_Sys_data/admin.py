from django.contrib import admin
from Henhouse_Sys_data import models
# Register your models here.

class partadmin(admin.ModelAdmin):
    list_display = [('part')]
    search_fields = [('part')]
class part_useradmin(admin.ModelAdmin):
    list_display = [('name')]
    search_fields = [('name')]
class companyadmin(admin.ModelAdmin):
    list_display = [('name')]
    search_fields=[('name')]
class barn_dataadmin(admin.ModelAdmin):
    list_display = [('company')]
    search_fields = [('company')]
class muenadmin(admin.ModelAdmin):
    list_display = [('name')]
    search_fields = [('name')]

class notice_infoadmin(admin.ModelAdmin):
    list_display = [('title')]
    search_fields = [('title')]
admin.site.register(models.part,partadmin)
admin.site.register(models.party_user,part_useradmin)
admin.site.register(models.company,companyadmin)
admin.site.register(models.barn_data,barn_dataadmin)
admin.site.register(models.muen,muenadmin)
admin.site.register(models.notice_info,notice_infoadmin)