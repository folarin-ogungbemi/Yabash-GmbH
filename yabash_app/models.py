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
    ("Birthday Party", "Birthday Party"),
    ("Meeting", "Meeting"),
    ("Ceremony", "Ceremony"),
    ("Private Reservation", "Private Reservation"),
]

TABLE_STATUS = ((0, "Available"), (1, "Occupied"))


# Create an Hour Entitiy for selceted hours for each Table in the Restaurant
class Hour(models.Model):
    hour_ID = models.CharField(max_length=2, primary_key=True, default="0H")
    hour = models.CharField(max_length=10, choices=HOURS, unique=True)
    booked_hour = models.BooleanField(default=False)
    hour_status = models.IntegerField(choices=TABLE_STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['hour_ID']

    def __str__(self):
        return f"{self.hour}"


# Create a Table Entity each with an ID keyed
# for the specific number of guests during Booking
class Table(models.Model):
    table_ID = models.IntegerField(primary_key=True, default=0000)
    capacity = models.CharField(
        max_length=10,
        choices=CAPACITY,
        unique=True)
    hour_ID = models.ManyToManyField(Hour)
    booked_table = models.BooleanField(default=False)
    table_status = models.IntegerField(choices=TABLE_STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['table_ID']

    def __str__(self):
        return f"{self.capacity}"


# Booking system for users
class Booking(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_reservation")
    number_of_guest = models.OneToOneField(
        Table,
        on_delete=models.CASCADE,
        related_name="table_capacity")
    event_date = models.DateField(default=datetime.now)
    event_time = models.OneToOneField(
        Hour,
        on_delete=models.CASCADE)
    event_type = models.CharField(
        choices=EVENTS,
        max_length=20,
        default="Birthday Party")
    event_info = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.client} | {self.number_of_guest} | {self.event_date} | {self.event_time}"
