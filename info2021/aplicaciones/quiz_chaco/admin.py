from django.contrib import admin
from .models import Pregunta
    # Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

    admin.site.register(Pregunta)
