from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title',  'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

    


admin.site.register(models.Category)
