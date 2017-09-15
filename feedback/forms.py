from django import forms
from . models import Feedback
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator
from capstone.models import Employee
import datetime


class FeedbackAddForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 20}),
                            validators=[EmailValidator(), MinLengthValidator(5), MaxLengthValidator(100)])
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 30, 'style': 'resize:none;'}))

    def clean_emp_no(self):
        print self.cleaned_data
        emp_no = self.cleaned_data.get('emp_no')

        if emp_no and not Employee.objects.filter(pk=emp_no).exists():
            raise forms.ValidationError('Invalid employee number')
        return self.cleaned_data.get('emp_no')

    class Meta:
        model = Feedback
        fields = ('emp_no', 'name', 'subject', 'category', 'email', 'comment', 'has_read', 'created_on')


class FeedbackForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 30, 'style': 'resize:none;'}))
    created_on = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Feedback
        fields = '__all__'
