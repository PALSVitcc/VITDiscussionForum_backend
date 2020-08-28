from django.db import models

class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    about = models.TextField()
    rating = models.FloatField()
    # bookmarks = models.ForeignKey(Question,on_delete=models.CASCADE)
class Question(models.Model):
    question = models.CharField(max_length=256)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.TimeField(auto_now=True)

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=512)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

class AnswerReplies(models.Model):
    replier = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.CharField(max_length=256)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

class Tags(models.Model):
    name = models.CharField(max_length=256)