from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    task_created = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    task_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return f"{self.content} (Tags: {self.tags}"
