# function that runs in admin.py(?)

def mark_feedback_as_read(modeladmin, request, queryset):
    for employeeFeedback in queryset:
        employeeFeedback.is_read = True
        employeeFeedback.save()


mark_feedback_as_read.short_description = 'Mark selected as read'
