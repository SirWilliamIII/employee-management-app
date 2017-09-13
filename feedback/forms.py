from django import forms
from . models import Feedback
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator


class FeedbackAddForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 60}),
                            validators=[EmailValidator(), MinLengthValidator(6), MaxLengthValidator(200)])
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 30, 'style': 'resize:none;'}))

    class Meta:
        model = Feedback
        fields = ('name', 'subject', 'category', 'email', 'comment', 'has_read',)


class FeedbackForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 30, 'style': 'resize:none;'}))
    created_on = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': '64'}))

    class Meta:
        model = Feedback
        fields = '__all__'
