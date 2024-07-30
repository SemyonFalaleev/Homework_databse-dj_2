
from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article

def test(request):
    ordering = '-published_at'
    object_list = Article.objects.order_by(ordering)
    tag_list = []
    for article in object_list:
        for scope in article.scopes.all():
            if scope.is_main:
                tag_list.append(scope.tag.name)  
    return HttpResponse(tag_list)

def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_list = Article.objects.order_by(ordering)
    context = {
        "object_list": object_list,
    }

    return render(request, template, context)
