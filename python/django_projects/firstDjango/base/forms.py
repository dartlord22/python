from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  # give me all of the fields form our Room class to fill out on the form
