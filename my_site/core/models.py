from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator
# from my_site.storage_backends import MediaStorage
# from django.db.models.signals import post_save, post_delete


class Tag(models.Model):
    caption = models.CharField(max_length= 20)

    def __str__(self):
        return f"{self.caption}"
    
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email_address = models.EmailField(max_length=254)
    
    @admin.display(description="Full name")
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.full_name()}"
    
class Post(models.Model):

    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    images = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tag = models.ManyToManyField(Tag)
    user_id = models.CharField(max_length=50, default=1)
    
    
    def __str__(self):
        return f"{self.title} {self.images} {self.date} {self.slug}"

class Comment(models.Model):
    
    user_name = models.CharField(max_length=120, verbose_name='User Name')
    user_email = models.EmailField(max_length=254, verbose_name='User Email')
    text = models.TextField(max_length=400, verbose_name='Comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f"{self.user_name} {self.user_email} {self.text}"
