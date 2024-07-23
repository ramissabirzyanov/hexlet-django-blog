from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from django.contrib import messages
from hexlet_django_blog.article.models import Article, ArticleComment
from .forms import ArticleCommentForm, ArticleForm



class IndexView(View):

    def get(self, request, *args, **kwargs):
            articles = Article.objects.all()[:15]
            return render(request, 'articles/index.html', context={
                'articles': articles,
            })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        comments = article.comments.all()
        form =ArticleCommentForm()
        return render(request, 'articles/show.html', context={
                'article': article, 'comments': comments, 'form': form,
            })
    
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = article
            new_comment.save()
        return redirect(reverse('article_id', args=[article.id]))

class ArticleCreateView(View):
     
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', context={'form': form})


    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            messages.success(request, 'you did it!.')
            form.save()
            return redirect('articles') 
        messages.error(request, 'something is wrong!.')
        return render(request, 'articles/create.html', context={'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

    def post(self,request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'DONE!')
            return redirect(reverse('article_id', args=(article_id,)))
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})
    
class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'DELETED!')
        return redirect('articles')