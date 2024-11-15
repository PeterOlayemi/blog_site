from django.db import models

from account.models import User

# Create your models here.

STATUS = (
    ('DRAFT', 'DRAFT'),
    ('PUBLISH', 'PUBLISH'),
)

class Category(models.Model):
    name = models.CharField(max_length=19, unique=True)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='article_category')
    title = models.CharField(max_length=99, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images')
    status = models.CharField(max_length=19, choices=STATUS, default='DRAFT')
    likes = models.ManyToManyField(User, related_name='article_like', blank=True)
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + ' by ' + self.writer.username
    
    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='replies')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.writer + ' comments - ' + self.content

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    
class Team(models.Model):
    image = models.ImageField(upload_to='team_images')
    full_name = models.CharField(max_length=99)
    role = models.CharField(max_length=99)
    bio = models.TextField(max_length=199)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

class Contact(models.Model):
    address = models.CharField(max_length=99)
    phone = models.CharField(max_length=19)
    email = models.EmailField(max_length=99)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
