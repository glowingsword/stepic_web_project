from django.conf.urls import patterns, include, url
from qa.views import test, page404, question_details, questions_list_all, questions_list_popular, ask_view, answer_add, signup, login
from django.contrib import admin

urlpatterns = patterns('',
   url(r'^$', questions_list_all, name='questions_list_all'),
   url(r'^login/', login, name='login'),
   url(r'^signup/', signup, name='signup'),
   url(r'^question/(?P<id>\d+)/', question_details, name='question_details'),
   url(r'^popular/$', questions_list_popular, name='questions_list_popular'),
   url(r'^ask/', ask_view, name='ask_view'),
   url(r'^answer/', answer_add, name='answer_add'),
   url(r'^new/', test, name='new'),
)
