from django.shortcuts import get_object_or_404
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Question
from .models import Answer



class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError(u'Title is empty', code='invalid')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(u'Text is empty', code='invalid')
        return text

    def save(self):
        self.cleaned_data['author_id'] = 1
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(u'Text is empty', code='invalid')
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(u'Question number incorrect',
                                        code='invalid')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question, pk=self.cleaned_data['question'])
        self.cleaned_data['author_id'] = 1
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
