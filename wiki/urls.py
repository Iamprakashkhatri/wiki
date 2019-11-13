from django.contrib import admin
from django.urls import path
from .views import add_article, edit_article, article_history, ArticleList, ArticleDetail
app_name='wiki'

urlpatterns = [
    path('', ArticleList.as_view(), name='wiki_article_index'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='wiki_article_detail'),
    path('history/<slug:slug>', article_history, name='wiki_article_history'),
    path('add/article', add_article, name='wiki_article_add'),
    path('edit/article/<slug:slug>', edit_article, name='wiki_article_edit'),
]
