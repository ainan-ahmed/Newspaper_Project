from django import template
from ..models import Article
from django.db.models import Count
register = template.Library()


@register.inclusion_tag('articles/latest_articles.html')
def latest_articles(count=3):
    latest = Article.published_article.order_by('-published')[:count]

    return {'latest': latest}


@register.inclusion_tag('articles/popular_articles.html')
def popular_articles(count=3):
    popular = Article.published_article.annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:count]

    return {'popular': popular}

