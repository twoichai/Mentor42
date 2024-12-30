from django.forms import ModelForm
from .models import Room, User, UserDetails
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']


class UserDetailsForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'
        exclude = ['is_online', 'is_verified', 'last_time_online', 'user', 'profile_picture', 'date_of_birth']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

