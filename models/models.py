from django.db import models

class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    about = models.TextField()
    rating = models.FloatField()
    # bookmarks = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=256)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.TimeField(auto_now=True)
    def __str__(self):
        return self.question

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=512)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

    def __str__(self):
        return  self.answer

class AnswerReplie(models.Model):
    replier = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.CharField(max_length=256)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

    def __str__(self):
        return self.reply

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.user + self.question

