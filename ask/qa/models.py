from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=255, default='')
  text = models.TextField(default='')
  added_at = models.DateTimeField(default=timezone.now)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User, related_name="question_author")
  likes = models.ManyToManyField(User, related_name="question_likes", blank=True)
  class Meta:
    ordering = ('added_at',)
  def __unicode__(self):
    return self.title
  def get_url(self):
    return reverse('question_details', kwargs={'pk': self.pk})

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(default=timezone.now)
  question = models.ForeignKey(Question,null=True)
  author = models.ForeignKey(User, null=True)
  class Meta:
    ordering = ('added_at',)
  def __unicode__(self):
    return self.title
  def get_url(self):
    return '/question/%s/' % self.question.id
