from django.contrib import admin
from dataManage import models
# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display = [('name'),]
class bikeadmin(admin.ModelAdmin):
    list_display = [('suffixURL'),]
class ensureadmin(admin.ModelAdmin):
    list_display = [('title')]
class fufendamin(admin.ModelAdmin):
    list_display = [('star_Id')]
class articleadmin(admin.ModelAdmin):
    list_display = [('title')]
class labeladmin(admin.ModelAdmin):
    list_display = [('label')]
class commentadmin(admin.ModelAdmin):
    list_display = [('content')]
class clifyadmin(admin.ModelAdmin):
    list_display = [('name')]
admin.site.register(models.user1,useradmin)
admin.site.register(models.boke,bikeadmin)
admin.site.register(models.fufen,fufendamin)
admin.site.register(models.article,articleadmin)
admin.site.register(models.article_nr,)
admin.site.register(models.article_zan)
admin.site.register(models.label,labeladmin)
admin.site.register(models.comment,commentadmin)
admin.site.register(models.ensure,ensureadmin)
admin.site.register(models.clify,clifyadmin)

