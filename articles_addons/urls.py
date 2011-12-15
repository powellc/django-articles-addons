# Adding URLs for django-articles CRUD
from django.conf.urls.defaults import *
from articles_addons.views import ArticleUpdateView, ArticleCreateView, ArticleDeleteView

urlpatterns = patterns('',
    url(r'^all/$', views.display_article, name='articles_list_articles'),
    url(r'^add/$', ArticleCreateView, name='articles_create_article'),
    url(r'^(?P<year>\d{4})/(?P<slug>.*)/update/$', ArticleUpdateView, name='articles_update_article'),
    url(r'^(?P<year>\d{4})/(?P<slug>.*)/delete/$', ArticleDeleteView, name='articles_delete_article'),
)
