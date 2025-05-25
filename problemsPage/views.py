
from django.shortcuts import render
from .models import Problem, Tag ,CodeSnippet
from django.shortcuts import get_object_or_404


# view to display problems with filtering by tags


def problems_list(request):
    tag_filter = request.GET.get('tag')
    if tag_filter:
        problems = Problem.objects.filter(tags__name=tag_filter)
    else:
        problems = Problem.objects.all()
    tags = Tag.objects.all()
    return render(request, 'problems_page/problems_page.html', {'problems': problems, 'tags': tags})

# Problem detail view

def problem_detail(request, slug):
    problem = get_object_or_404(Problem, slug=slug)
    # Optional: Let user select language from query param (?lang=cpp)
    language = request.GET.get('lang', 'python')  # Default to Python

    # Try to get the code snippet for selected language
    try:
        code_snippet = problem.code_snippets.get(language=language).snippet
    except CodeSnippet.DoesNotExist:
        code_snippet = "# Code snippet not available for selected language"

    return render(request, 'problems_page/problem_detail.html', {
        'problem': problem,
        'code_snippet': code_snippet,
        'language': language,
    })
