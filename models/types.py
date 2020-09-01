import graphene
from graphene_django import DjangoObjectType
from models.models import *

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id","username" ,"first_name","last_name", "about","rating","password")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "question", "author", "timestamp")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "user", "question","answer", "upvotes","downvotes")