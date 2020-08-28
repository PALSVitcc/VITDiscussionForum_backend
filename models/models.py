from django.db import models
from django.contrib.auth.models import AbstractUser

class Tags(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    about = models.TextField(
        max_length=500,
    )
    rating = models.FloatField(default=0.0)
    bookmarks = models.ManyToManyField(Tags)
    def _str_(self):
        return "{} - {} {} ({})".format(
            self.username, self.first_name, self.last_name
        )
class Question(models.Model):
    question = models.CharField(max_length=300)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Question_Author")
    timestamp = models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.question

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.TextField(default="")
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    timestamp = models.TimeField(auto_now=True)

    def __str__(self):
        return self.answer

class AnswerReply(models.Model):
    replier = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reply_user")
    reply = models.TextField()
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer