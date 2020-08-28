import graphene
from graphene_django import DjangoObjectType
from models.models import *
from .types import *

class UserQuery(graphene.ObjectType):
    all_user = graphene.List(UserType)
    category_by_name = graphene.Field(UserType, name=graphene.String(required=True))
    def resolve_all_user(root, info):
        return User.objects.all()
    def resolve_category_by_name(root, info, name):
        try:
            return User.objects.get(name=name)
        except User.DoesNotExist:
            return None

class AnswerQuery(graphene.ObjectType):
    all_answers = graphene.List(AnswerType)
    category_by_name = graphene.Field(AnswerType, name=graphene.String(required=True))
    def resolve_all_answers(root, info):
        return Answer.objects.all()
    def resolve_category_by_name(root, info, name):
        try:
            return Answer.objects.get(answer=name)
        except Answer.DoesNotExist:
            return None

class QuestionQuery(graphene.ObjectType):
    all_question = graphene.List(QuestionType)
    category_by_name = graphene.Field(QuestionType, name=graphene.String(required=True))
    def resolve_all_question(root, info):
        return Question.objects.all()
    def resolve_category_by_name(root, info, name):
        try:
            return Question.objects.get(question=name)
        except Question.DoesNotExist:
            return None
class SuperClass(UserQuery,QuestionQuery,AnswerQuery):
    pass

schema = graphene.Schema(query=SuperClass)
