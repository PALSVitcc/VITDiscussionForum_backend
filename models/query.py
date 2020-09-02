import graphene
from .models import *
from .object_types import (
    TagsType,
    UserType,
    AnswerType,
    QuestionType,
    AnswerReplyType
)

class Query(object):

    tags = graphene.List(
        TagsType,
        ids=graphene.List(
            graphene.NonNull(graphene.Int),
        ),
        name_iexact=graphene.String(),
        name_icontains=graphene.String()
    )

    def resolve_tags(self,info, **kwargs):

        if info.context.user.is_anonymous:
            queryset = Tags.objects.all()
            if kwargs.get("ids"):
                queryset.filter(id__in=kwargs.get("ids"))
            if kwargs.get("name_iexact"):
                queryset.filter(name__iexact=kwargs.get("name_iexact"))
            if kwargs.get("name_icontains"):
                queryset.filter(name__icontains=kwargs.get("name_icontains"))
            return queryset
        return None

    all_user = graphene.List(
        UserType,
        username=graphene.String(),
    )
    # category_by_name = graphene.Field(UserType, name=graphene.String(required=True))
    def resolve_all_user(self, info, **kwargs):
        username  = kwargs.get("username")
        userInstance = User.objects.all()
        if username:
            userInstance = userInstance.filter(username__iexact=username)
        return userInstance
    


# class AnswerQuery(graphene.ObjectType):
#     all_answers = graphene.List(AnswerType)
#     category_by_name = graphene.Field(AnswerType, name=graphene.String(required=True))
#     def resolve_all_answers(root, info):
#         return Answer.objects.all()
#     def resolve_category_by_name(root, info, name):
#         try:
#             return Answer.objects.get(answer=name)
#         except Answer.DoesNotExist:
#             return None

# class QuestionQuery(graphene.ObjectType):
#     all_question = graphene.List(QuestionType)
#     category_by_name = graphene.Field(QuestionType, name=graphene.String(required=True))
#     def resolve_all_question(root, info):
#         return Question.objects.all()
#     def resolve_category_by_name(root, info, name):
#         try:
#             return Question.objects.get(question=name)
#         except Question.DoesNotExist:
#             return None