from django import forms
from .models import *
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"
    
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = (
            "name",
            "pub_date",
            "image",
            "host",
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pub_date"].widget = DateTimeInput()
        self.fields["pub_date"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        
    def is_valid(self):
        is_valid = super(GameForm,self).is_valid()
        if not is_valid:
            for field in self.errors.keys():
                print ("ValidationError: %s[%s] <- \"%s\" %s" % (
                    type(self),
                    field,
                    self.data[field],
                    self.errors[field].as_text()
                ))
        return is_valid

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'discordId',
        )
        
class WinnersForm(forms.ModelForm):
    class Meta:
        model = Winners
        fields =(
            'position',
            'game',
            'player'
        )