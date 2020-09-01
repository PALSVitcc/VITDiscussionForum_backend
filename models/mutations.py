from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from .types import *

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        about = graphene.String(required=True)        

    def mutate(self, info, username, password, email,about,last_name,first_name):
        user = get_user_model()(
            username=username,
            email=email,
            about=about,
            last_name=last_name,
            first_name=first_name
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()