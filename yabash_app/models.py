from django.db import models
from django.contrib.auth.models import User


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
