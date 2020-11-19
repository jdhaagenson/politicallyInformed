from django import forms

from voters.models import Voter

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterVoter(forms.ModelForm):
    class Meta:
        model = Voter
        fields = [
            'image',
            'email',
            'username',
            'password1',
            'password2',
            'gender',
            'party'
        ]


