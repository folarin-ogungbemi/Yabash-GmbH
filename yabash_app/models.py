from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


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
CAPACITY = [
    ("1 Person", "1 Person"),
    ("2 People", "2 People"),
    ("3 People", "3 People"),
    ("4 People", "4 People"),
    ("5 People", "5 People"),
    ("6 People", "6 People"),
    ("7 People", "7 People"),
    ("8 People", "8 People"),
    ("9 People", "9 People"),
    ("10 People", "10 People"),
    ]

HOURS = [
    ("08:00 am", "08:00 am"),
    ("10:00 am", "10:00 am"),
    ("12:00 pm", "12:00 pm"),
    ("14:00 pm", "14:00 pm"),
    ("16:00 pm", "16:00 pm"),
    ("18:00 pm", "18:00 pm"),
    ("20:00 pm", "20:00 pm"),
    ("22:00 pm", "22:00 pm"),
]

EVENTS = [
    ("BP", "Birthday Party"),
    ("M", "Meeting"),
    ("C", "Ceremony"),
    ("PR", "Private Reservation"),
]


# The Table Entity should be tracked
class Table(models.Model):
    capacity = models.CharField(
        choices=CAPACITY,
        max_length=10)
    available = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.capacity}"


# Booking system for users
class Booking(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_reservation",
        null=False,
        blank=False)
    number_of_guest = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="table_capacity",
        null=False,
        blank=False,
        default="")
    event_date = models.DateField(default=datetime.now)
    event_time = models.CharField(
        choices=HOURS,
        max_length=10,
        default="10:00 am")
    event_type = models.CharField(
        choices=EVENTS,
        max_length=20,
        default="Birthday Party")
    event_info = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.client} | {self.number_of_guest} | {self.event_date} | {self.event_time}"
