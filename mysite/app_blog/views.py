from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DateDetailView
from .models import Article

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class ArticleDetail(DateDetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'
    date_field = 'pub_date'
    query_pk_and_slug = True
    month_format = '%m'
    allow_future = True

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        try:
            context['images'] = context['item'].images.all()
        except:
            pass
        return context

class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        return context

class ArticleCategoryList(ListView):
    model = Article
    template_name = 'articles_category_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug'])
