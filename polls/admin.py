

from django.contrib import admin

from .models import Question,Choice


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Questions",  {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)