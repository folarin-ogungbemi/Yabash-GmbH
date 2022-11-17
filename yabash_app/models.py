from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Testimonial(models.Model):
    summary = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post_testimony")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.summary} Testimony {self.content} by {self.name}"


class Headline(models.Model):
    headline_text = models.CharField(max_length=200, unique=True)
    sub_text = models.CharField(max_length=200, unique=True)
    contact = models.CharField(max_length=50)
    reservation = models.CharField(max_length=50)
    images = CloudinaryField('image', default='placeholder')
    opening_time = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.headline_text
