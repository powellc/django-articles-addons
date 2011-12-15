# Views for article CRUD
from articles.models import Article
from articles_addons.forms import ArticleForm

class ArticleCreateView(CreateView):
    form_class=ArticleForm
    template_name='articles/post_create.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        return context

class ArticleUpdateView(UpdateView):
    form_class=ArticleForm
    template_name='articles/post_update.html'
    queryset=Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        return context

class ArticleDeleteView(DeleteView):
    model=Article
    template_name='articles/post_delete.html'
    success_url='/articles/' 
