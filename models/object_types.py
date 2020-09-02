import graphene
from graphene_django import DjangoObjectType
from models.models import *

class TagsType(DjangoObjectType):
    class Meta:
        model = Tags

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id","username" ,"first_name","last_name", "about","rating","email", "password")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer

class AnswerReplyType(DjangoObjectType):
    class Meta:
        model = AnswerReply