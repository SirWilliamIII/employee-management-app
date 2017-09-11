from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django import forms
from .models import Feedback


class FeedbackAddForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('name', 'subject', 'category', 'email', 'comment')


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'


def mark_feedback_as_read(queryset):
    for employeeFeedback in queryset:
        employeeFeedback.is_read = True
        employeeFeedback.save()


mark_feedback_as_read.short_description = 'Mark selected as read'


class FeedbackAdmin(ModelAdmin):
    form = FeedbackForm
    search_fields = ('name', 'category', 'email', 'subject')
    list_display = ('name', 'category', 'email', 'subject')
    save_on_top = True
    actions_on_bottom = False

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return FeedbackForm
        else:
            return super(FeedbackAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Feedback, FeedbackAdmin)
