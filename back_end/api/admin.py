from django.contrib import admin
from .models import Story, Fragment, Clue, Game, GamePartecipant, GameFragment


class StoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator_user', 'title']
    search_fields = ['title']


admin.site.register(Story, StoryAdmin)


class FragmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'story', 'location']
    search_fields = ['story']


admin.site.register(Fragment, FragmentAdmin)


class ClueAdmin(admin.ModelAdmin):
    list_display = ['id', 'fragment', 'fragment__story']
    search_fields = ['fragment__story']

    def fragment__story(self, obj):
        return obj.fragment.story


admin.site.register(Clue, ClueAdmin)

admin.site.register(Game)
admin.site.register(GamePartecipant)
admin.site.register(GameFragment)
