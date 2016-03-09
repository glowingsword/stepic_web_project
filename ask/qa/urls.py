from django.conf.urls import patterns, include, url
from qa.views import test, question, page404

urlpatterns = [                                                                 
   url(r'^$', test, name='index'),                                              
   url(r'^login/', test, name='login'),                                         
   url(r'^signup/', test, name='signup'),                                       
   url(r'^question/(?P<id>\d+)/', question, name='question'),                   
   url(r'^ask/', test, name='ask'),                                             
   url(r'^popular/', test, name='popular'),                                     
   url(r'^new/', test, name='new'),                                             
]
