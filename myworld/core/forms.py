from django.forms import ModelForm
from .models import Profile

class ProfileForn(ModelForm):
    class Meta:
        model = Profile
        exclude=['uuid']
        