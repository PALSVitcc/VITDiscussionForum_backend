from django.contrib.auth import get_user_model
import graphene
from .models import *
from .object_types import (
    TagsType,
    UserType,
    QuestionType,
    AnswerType,
    AnswerReplyType
)


class CreateTags(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    tag = graphene.Field(TagsType, name="tag")
    errors = graphene.String()

    def mutate(self, info, name=None):
        user = info.context.user

        is_existing = (
            True if len(Tags.objects.filter(name=name)) > 0 else False 
        )

        if is_existing:
            return CreateTags(
                tag=None, 
                errors="Tag Already Exixts."
            )
        if user:
            try:
                tagInstance = Tags(name=name)
                tagInstance.save()
            
            except Exception as err:
                return CreateTags(
                    tag=None, errors=str(err)
                )
            return CreateTags(
                tag=tagInstance, errors=None
            )
        return CreateTags(
            tag=None, errors="Insufficient Privileges"
        )

class UpdateTag(graphene.Mutation):
    class Arguments:
        id=graphene.Int(required=True)
        name=graphene.String(required=True)
    
    tag = graphene.Field(TagsType, name="tag")
    errors = graphene.String()

    def mutate(self,info,name=None,id=None):
        user = info.context.user
        try:
            tagInstance = Tags.objects.get(pk=id)
        except Tags.DoesNotExist:
            return UpdateTag(
                tag=None,
                errors="Tags Not Found"
            )
        
        try:
            tagInstance.name = name
            tagInstance.save()
        except Exception as err:
            return UpdateTag(
                tag=None,
                errors=str(err)
            )
        return UpdateTag(
                tag=tagInstance,
                errors=None
            )

class DeleteTags(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    
    tag = graphene.Field(TagsType, name="tag")
    errors = graphene.String()

    def mutate(self,info,id=None):
        try:
            tagInstance = Tags.objects.get(pk=id)
        except Tags.DoesNotExist:
            return UpdateTag(
                tag=None,
                errors="Tags Not Found"
            )
        
        try:
            tagInstance.delete()
        except Exception as err:
            return UpdateTag(
                tag=None,
                errors=str(err)
            )

        return UpdateTag(
                tag=tagInstance,
                errors=None
            )

class CreateUser(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        confirm_password = graphene.String(required=True)
        email = graphene.String()
        about = graphene.String()   

    user = graphene.Field(UserType)
    errors = graphene.String()     

    def mutate(self, info, username, password,last_name,first_name,confirm_password, email=None,about=None):

        if password != confirm_password:
            return CreateUser(user=None, errors="Paswords Do Not Match")
        user = User.objects.create_user(
            username=username,
            email=email,
            about=about,
            last_name=last_name,
            first_name=first_name
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user,errors=None)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_tags = CreateTags.Field()
    update_tag = UpdateTag.Field()
    delete_tags = DeleteTags.Field()