from django.conf.urls import patterns, include, url
from qa.views import test, question, page404

urlpatterns = [
   url(r'^login/', page404, name='login'),
   url(r'^signup/', page404, name='signup'),
   url(r'^question/(?P<id>\d+)/', question, name='question'),
   url(r'^ask/', page404, name='ask'),
   url(r'^popular/', page404, name='popular'),
   url(r'^new/', page404, name='new'),
]
