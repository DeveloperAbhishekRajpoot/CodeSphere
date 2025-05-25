from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Problem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # e.g., "two-sum"
    difficulty = models.CharField(max_length=10, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    description = models.TextField()  # Markdown or HTML
    input_description = models.TextField()
    output_description = models.TextField()
    constraints = models.TextField()
    example_input_output = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class CodeSnippet(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('cpp', 'C++'),
        ('c', 'C'),
        ('java', 'Java'),
        ('javascript', 'JavaScript'),
    ]

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='code_snippets')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    snippet = models.TextField()  # The skeleton function/code

    class Meta:
        unique_together = ('problem', 'language')  # Only one snippet per language per problem

    def __str__(self):
        return f"{self.problem.title} - {self.language}"
