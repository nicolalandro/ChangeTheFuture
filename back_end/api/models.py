from django.db import models
from django.conf import settings


class Story(models.Model):
    creator_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='stories', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        unique_together = "creator_user", "title"

    def __str__(self):
        return f'{self.creator_user}/{self.title}'


class Fragment(models.Model):
    story = models.ForeignKey(Story, related_name='fragments', on_delete=models.CASCADE)

    text = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    is_ending = models.BooleanField(default=False)
    order_number = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.id}) {self.story.creator_user}/{self.story.title}'


class Clue(models.Model):
    fragment = models.OneToOneField(Fragment, related_name='clue', on_delete=models.CASCADE)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Game(models.Model):
    story = models.ForeignKey(Story, related_name='games', on_delete=models.CASCADE)
    creator_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='games', on_delete=models.CASCADE)

    is_running = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.creator_user}/{self.story.title}({self.id})'


class GamePartecipant(models.Model):
    game = models.ForeignKey(Game, related_name='game_partecipants', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='game_partecipants', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GameFragment(models.Model):
    game = models.ForeignKey(Game, related_name='game_fragments', on_delete=models.CASCADE)
    fragment = models.OneToOneField(Fragment, related_name='game_fragments', on_delete=models.CASCADE)

    is_covered = models.BooleanField(default=True)
    is_clue_covered = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
