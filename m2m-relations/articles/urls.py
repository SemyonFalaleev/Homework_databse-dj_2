from django.urls import path

from articles.views import articles_list, test

urlpatterns = [
    path('', articles_list, name='articles'),
    path('test/', test)
    
]
