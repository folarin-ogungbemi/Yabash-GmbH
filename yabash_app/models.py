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


# Defines the capacity of the tables in the restaurant
CAPACITY = (
    (1, "One"),
    (2, "Two"),
    (3, "Three"),
    (4, "Four"),
    (5, "Five"),
    (6, "Six"),
    (7, "Seven"),
    (8, "Eight"),
    (9, "Nine"),
    (10, "Ten"),
    )

TABLE_STATUS = ((0, "No"), (1, "Yes"))


# The Table Entity should be tracked
class Table(models.Model):
    capacity = models.IntegerField(choices=CAPACITY)
    available = models.BooleanField(default=False)
    availability = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    table_status = models.IntegerField(choices=TABLE_STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.capacity}"

    def check_table(self):
        if TABLE_STATUS == 1:
            return self.available


# Booking system for users
class Booking(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_reservation",
        null=False,
        blank=False)
    no_of_guest = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="table_capacity",
        null=False,
        blank=False)
    event_date = models.DateField(null=False, blank=False)
    event_time = models.TimeField(null=False, blank=False)
    event_type = models.CharField(max_length=100)
    event_info = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.no_of_guest}"
