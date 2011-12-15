from django.forms import ModelForm
from articles.models import Article

class ArticleForm(ModelForm):
  class Meta:
    model = Article
    exclude = ('sites', 'slug', 'is_active', 'login_required', 'followup_for', 'related_articles', 'keywords', 'description', 'auto_tag' )

