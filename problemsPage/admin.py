from django.contrib import admin
from problemsPage.models import Tag, Problem

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficulty')
    search_fields = ('title', 'description')
    list_filter = ('difficulty', 'tags')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)
