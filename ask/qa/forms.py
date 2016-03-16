from django import forms
from django.forms import ModelForm
from .models import Question
from .models import Answer

class AskForm(ModelForm):
  class Meta:
    model = Question
    fields = ['title', 'text']
    exclude = ('author',)

class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question', 'author']
