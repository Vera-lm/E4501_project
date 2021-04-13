from django.forms import ModelForm
from .models import Sighting


class SquirrelMap(ModelForm):
    class Meta:
        model = Sighting
        fields = [
                'squirrel'
                ]
