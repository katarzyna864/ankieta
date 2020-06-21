
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    voted_choice = models.ForeignKey(Choice, related_name='topic_content_type', on_delete=models.CASCADE,)
    voted_question = models.ForeignKey(Question, related_name='topic_content_type', on_delete=models.CASCADE,)
    date = models.CharField(max_length=200)
    voted_answer = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)
    def __str__(self):
        return self.date

class Vote2(models.Model):
    voted_choice = models.ForeignKey(Choice, related_name='topic_content_type2', on_delete=models.CASCADE,)
    voted_question = models.ForeignKey(Question, related_name='topic_content_type2', on_delete=models.CASCADE,)
    date = models.CharField(max_length=200)
    voted_answer = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)
    def __str__(self):
        return self.date

class User(models.Model):
    username = models.CharField(max_length=200)
    question = models.CharField(max_length=5)
    def __str__(self):
        return self.username

class User2(models.Model):
    username = models.CharField(max_length=200)
    question = models.CharField(max_length=5)
    def __str__(self):
        return self.username

class Test(models.Model):
    user_id = models.CharField(max_length=200)
    def __str__(self):
        return self.user_id