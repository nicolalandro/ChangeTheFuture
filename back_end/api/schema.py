import graphene
from graphene_django import DjangoObjectType
from .models import Story, Fragment, Clue, Game, GamePartecipant, GameFragment


class StoryType(DjangoObjectType):
    class Meta:
        model = Story


class FragmentType(DjangoObjectType):
    class Meta:
        model = Fragment


class ClueType(DjangoObjectType):
    class Meta:
        model = Clue


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class GamePartecipantType(DjangoObjectType):
    class Meta:
        model = GamePartecipant


class GameFragmentType(DjangoObjectType):
    class Meta:
        model = GameFragment


class Query(graphene.ObjectType):
    stories = graphene.List(StoryType)
    fragments = graphene.List(FragmentType)
    clues = graphene.List(ClueType)
    games = graphene.List(GameType)
    game_partecipants = graphene.List(GamePartecipantType)
    game_fragments = graphene.List(GameFragmentType)

    def resolve_stories(self, info, **kwargs):
        return Story.objects.all()

    def resolve_fragments(self, info, **kwargs):
        return Fragment.objects.all()

    def resolve_clues(self, info, **kwargs):
        return Clue.objects.all()

    def resolve_games(self, info, **kwargs):
        return Game.objects.all()

    def resolve_game_partecipants(self, info, **kwargs):
        return GamePartecipant.objects.all()

    def resolve_game_fragments(self, info, **kwargs):
        return GameFragment.objects.all()


schema = graphene.Schema(query=Query)
