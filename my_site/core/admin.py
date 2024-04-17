from django.contrib import admin
from .models import Tag, Author, Post
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


  
  
@admin.register(Author)   
class AuthorAdmin(admin.ModelAdmin):
   
    list_display = ["full_name", "email_address"]
    


@admin.register(Post)    
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","slug", "author", "date","image_name"]
   #field = ["title", "slug","excerpt", "image_name", "date", "content", "tag"]
    list_filter = ["author", "tag", "date"]
    filter_horizontal= [("tag"),]
    prepopulated_fields = {"slug": ["title"]}
    radio_fields = {"author":admin.VERTICAL}