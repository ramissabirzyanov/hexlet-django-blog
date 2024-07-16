from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class IndexView(View):


    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html', context={'article_tags':'python', 'article_id':42})


def make_redirect(request):
    url_redirect = reverse('article', kwargs={'article_tags':'python', 'article_id':42})
    return redirect(url_redirect)
