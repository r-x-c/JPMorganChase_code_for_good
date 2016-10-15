from django.contrib import admin
from .models import AnswerT
from .models import QuestionT
from .models import UserT


class AnswerInline(admin.StackedInline):
    model = AnswerT
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['q_text', 'hero']}),
    ]
    inlines = [AnswerInline]

admin.site.register(QuestionT, QuestionAdmin)

admin.site.register(UserT)


# Register your models here.


