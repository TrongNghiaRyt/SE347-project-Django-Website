from django.contrib import admin
from .models import *

class Answers(admin.TabularInline):
    model = Answer

admin.site.site_header = 'VehiTest admin'

class QuestionAndAnswers(admin.ModelAdmin):
    inlines = [Answers]
    list_display = ('id', 'kind', 'content')

    list_filter = ('kind',)
    fields = (
        'content',
        'pic',
        'kind',
    )
class kind(admin.TabularInline):
    model = QuestionType

class Examination(admin.ModelAdmin):
    inlines = [kind]

    fieldsets = (
        (None, {
            "fields": (
                'name',
                'exam_times',
                'question_number',
                'question_correct',
            ),
        }),
    )
    
admin.site.register(Question, QuestionAndAnswers)
admin.site.register(exam, Examination)
admin.site.register(Answer)


