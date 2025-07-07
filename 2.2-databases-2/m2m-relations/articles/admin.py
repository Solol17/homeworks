from django.contrib import admin
from .models import Article, Category, MainCategoryArticles

class MainCategoryInline(admin.TabularInline):
    model = MainCategoryArticles
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['title']
    inlines = [MainCategoryInline,]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id',]

