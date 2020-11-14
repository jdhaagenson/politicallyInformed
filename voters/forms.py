from django import forms


class RegisterVoter(forms.ModelForm):
    class Meta:
        fields = [
            'email',
            'username',
            'password1',
            'password2',
            'gender',
            'party'
        ]


class EditProfilePhoto(forms.Form):
    image = forms.ImageField