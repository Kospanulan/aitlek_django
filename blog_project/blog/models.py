from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}\n{self.text}"


class Comment(models.Model):

    text = models.CharField(max_length=100)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


class Tag(models.Model):

    name = models.CharField(max_length=100)

    posts = models.ManyToManyField(Post, related_name="tags")





"""
primary key - pk
foreign key - fk

contains = подстороки

gt - greater than
gte - greater than or equal

lt - less than
lte - less than or equal

in - title__in=["title1", "title2"]

"""