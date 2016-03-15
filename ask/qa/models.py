from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(default=timezone.now)
  rating = models.IntegerField(blank=True)
  author = models.ForeignKey(User, blank=True)
  likes = models.ManyToManyField(User, related_name="question_likes", blank=True)
  class Meta:
    ordering = ('added_at',)
    def __unicode__(self):
      return self.title
    def get_url(self):
      return '/question/%s/' % self.id

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(default=timezone.now)
  question = models.OneToOneField(Question, blank=True)
  author = models.ForeignKey(User, null=True)
  class Meta:
    ordering = ('added_at',)
    def __unicode__(self):
      return self.title
    def get_url(self):
      return '/question/%s/' % self.id
