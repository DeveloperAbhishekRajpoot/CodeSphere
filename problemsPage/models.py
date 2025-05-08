
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # e.g., "two-sum"
    difficulty = models.CharField(max_length=10, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    description = models.TextField()  # You can use Markdown or rich HTML
    input_description = models.TextField()
    output_description = models.TextField()
    constraints = models.TextField()
    example_input_output = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
