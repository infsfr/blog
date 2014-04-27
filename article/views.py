from django.shortcuts import render
from article.models import Article, Comments


def articles(request):
    return render(request, 'articles.html', {
        'articles': Article.objects.all(),
    })


def article(request, article_id=1):
    print dir(Article.objects.get(id=article_id))
    return render(request, 'article.html', {
        'article': Article.objects.get(id=article_id),
        'comments': Comments.objects.filter(comments_article_id=article_id),
    })
