from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(max_length=250)
    answers = forms.ChoiceField(choices=(''))