from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField('add comment', max_length=100)

    def __str__(self):
        return self.content
 