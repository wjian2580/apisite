from django.contrib import admin

# Register your models here.
from polls.models import Question,Choice

# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['question_text', 'pub_date']

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'day_before')
	fieldsets = [
		('text',{'fields': ['question_text']}),
		('date imformation', {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
