from django.contrib import admin
from .models import Idea, Location


class LocationInline(admin.StackedInline):
    model = Location
    extra = 1


class IdeaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['link', "place"]}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [LocationInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')


# adminページにIdeaAdminの表示形式でIdeaモデルを記載する
admin.site.register(Idea, IdeaAdmin)
