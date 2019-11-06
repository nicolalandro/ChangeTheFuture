from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from api.schema import schema
from serve_front_end.views import IndexView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', csrf_exempt(GraphQLView.as_view(schema=schema, graphiql=True)))
]
