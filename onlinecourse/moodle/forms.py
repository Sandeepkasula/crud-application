from django import forms
from .models import moodle
class moodleform(forms.ModelForm):
    class Meta:
        model = moodle
        fields = '__all__'