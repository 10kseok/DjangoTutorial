from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    # Inline도 종류가 있음.
    # StackedInline -> [choice 1 text, votes] [choice 2 text, votes]  ...
    # TabularInline -> [choice [text1 vote1] [text2 vote2] ...]
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)