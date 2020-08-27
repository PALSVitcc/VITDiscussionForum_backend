from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
]
