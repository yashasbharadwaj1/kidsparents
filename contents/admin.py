from django.contrib import admin
from . import models
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }
admin.site.register(models.Category)
admin.site.register(models.places)
admin.site.register(models.bloodbank)
admin.site.register(models.blooddonors)