from django.shortcuts import render
from django.http import Http404

from .models import Article


def archive(request):
    posts = Article.objects.all()

    context = {
        'posts': posts
    }

    return render(
        request,
        'archive.html',
        context
    )


def get_article(request, article_id):

    try:
        post = Article.objects.get(id=article_id)

        context = {
            'post': post
        }

        return render(
            request,
            'article.html',
            context
        )

    except Article.DoesNotExist:
        raise Http404("Статья не найдена")
