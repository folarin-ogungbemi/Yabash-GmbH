from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    name = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="post_testimony",
        null=False,
        blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.summary} by {self.name}"
