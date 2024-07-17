from django.contrib import admin

# Register your models here.
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']
    list_display = ('name', 'created_at')
    list_filter = (('created_at', admin.DateFieldListFilter),)



