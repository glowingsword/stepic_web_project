from django.conf.urls import patterns, include, url
from qa.views import test, question, page404

urlpatterns = [
   url(r'^$', questions_list_all, name='questions_list_all'),
   url(r'^question/(?P<id>\d+)/', question_details, name='question_details'),
   url(r'^popular/$', questions_list_popular, name='questions_list_popular),
   url(r'^ask/', test, name='ask'),
   url(r'^new/', test, name='new'),
   url(r'^login/', test, name='login'),
   url(r'^signup/', test, name='signup'),
]
