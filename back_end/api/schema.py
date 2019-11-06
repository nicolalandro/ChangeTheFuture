import graphene
from graphene_django import DjangoObjectType
from .models import Story, Fragment, Clue, Game, GamePartecipant, GameFragment


class StoryType(DjangoObjectType):
    class Meta:
        model = Story


class FragmentType(DjangoObjectType):
    class Meta:
        model = Fragment


class Query(graphene.ObjectType):
    stories = graphene.List(StoryType)
    fragments = graphene.List(FragmentType)

    def resolve_stories(self, info, **kwargs):
        return Story.objects.all()

    def resolve_fragments(self, info, **kwargs):
        return Fragment.objects.all()


schema = graphene.Schema(query=Query)
