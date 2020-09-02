import graphene
from .query import Query as query
from .mutations import Mutation as mutation

class Query(query,graphene.ObjectType):
    pass

class Mutation(mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)