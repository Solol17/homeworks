from django.shortcuts import render
from llm.cli import models
from django.db.models import Prefetch


from articles.models import Article, MainCategoryArticles


def articles_list(request):
    template = 'articles/news.html'

    # Создаем Prefetch с нужной сортировкой
    scopes_prefetch = Prefetch(
        'scopes',
        queryset=MainCategoryArticles.objects.select_related('tag')
        .order_by('-is_main', 'tag__name')
    )

    object_list = Article.objects.prefetch_related(scopes_prefetch) \
        .order_by('-published_at')

    context = {'object_list': object_list}
    return render(request, template, context)
