from django.forms import ModelForm
from .models import Room, User, UserDetails


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
