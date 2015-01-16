from django.forms import ModelForm, RadioSelect
from .models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'gender', 'birth_date',
                  'phone_number', 'location')
