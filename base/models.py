from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="details")

    # Tracks user's online status or last online time
    is_online = models.BooleanField(default=False)
    last_time_online = models.DateTimeField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    date_of_birth = models.DateField(blank=True, null=True)
    preferred_language = models.CharField(max_length=10, blank=True, null=True)  # e.g., 'en', 'de', 'fr'
    country = CountryField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True, max_length=500)

    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)

    # Social Media
    github_profile = models.URLField(max_length=200, blank=True, null=True)
    instagram_profile = models.URLField(max_length=200, blank=True, null=True)
    linkedin_profile = models.URLField(max_length=200, blank=True, null=True)

    # Mentor Program
    looking_for_mentor = models.BooleanField(default=False)
    mentor = models.BooleanField(default=False)

    # Interests (to be converted into tags later)
    interests = models.TextField(blank=True, null=True)  # Store as a comma-separated string for now

    class Meta:
        verbose_name = "User detail"
        verbose_name_plural = "User details"

    def __str__(self):
        return f"Details of {self.user.username}"
