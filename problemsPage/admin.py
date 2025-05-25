from django.contrib import admin
from problemsPage.models import Tag, Problem , CodeSnippet

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficulty')
    list_display_links = ('title',)  # <-- This makes the 'title' field clickable
    search_fields = ('title', 'description')
    list_filter = ('difficulty', 'tags')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)

@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ('problem', 'language')
    list_filter = ('language',)
    search_fields = ('problem__title', 'snippet')
