import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Vote(models.Model):
    voted_choice = models.ForeignKey(Choice, related_name='topic_content_type', on_delete=models.CASCADE)
    voted_question = models.ForeignKey(Question, related_name='topic_content_type', on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200)
    def __str__(self):
        return self.user_id

class User(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Test(models.Model):
    user_id = models.CharField(max_length=200)
    def __str__(self):
        return self.user_id