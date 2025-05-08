
from django.shortcuts import render
from .models import Problem, Tag
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
    return render(request, 'problems_page/problem_detail.html', {'problem': problem})
