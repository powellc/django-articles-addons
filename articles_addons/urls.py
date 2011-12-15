# Adding URLs for django-articles CRUD
from django.contrib.auth.decorators import login_required 
from django.conf.urls.defaults import *
from django.views.generic import ListView 
from articles_addons.views import ArticleUpdateView, ArticleCreateView, ArticleDeleteView
from articles.views import display_article

urlpatterns = patterns('',
    url(r'^all/$', login_required(ListView.as_view()), name='articles_list_articles'),
    url(r'^add/$', login_required(ArticleCreateView.as_view()), name='articles_create_article'),
    url(r'^(?P<year>\d{4})/(?P<slug>.*)/update/$', login_required(ArticleUpdateView.as_view()), name='articles_update_article'),
    url(r'^(?P<year>\d{4})/(?P<slug>.*)/delete/$', login_required(ArticleDeleteView.as_view)), name='articles_delete_article'),
)
