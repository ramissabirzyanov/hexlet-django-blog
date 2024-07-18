from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article, ArticleComment
from .forms import ArticleCommentForm



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

        
         
        


# class CommentArticleView(View):
#     def get(self, request, *args, **kwargs):
#         comments = ArticleComment.objects.all()
#         form = ArticleCommentForm()
#         return render(request, 'articles/comment.html', context={'form':form, 'comments':comments})

         

#     def post(self, request, *args, **kwargs):
#         form = ArticleCommentForm(request.POST)
#         article = get_object_or_404(Article, id=kwargs['id']) 
#         if form.is_valid(): 
#             form.save()
#         return redirect(reverse('article_id', args=article))
