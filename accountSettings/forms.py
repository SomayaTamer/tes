from django import forms
from .models import UserSettings

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['name', 'email', 'theme', 'notification_enabled', 'notification_sound', 'gender']
        widgets = {
            'gender': forms.RadioSelect,
            'theme': forms.Select,
        }