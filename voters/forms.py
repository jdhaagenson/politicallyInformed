from django import forms





class EditProfilePhoto(forms.Form):
    image = forms.ImageField(allow_empty_file=True)

