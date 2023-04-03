from django.shortcuts import render

from todo.models import Task


def index(request):
    context = {
        "tasks": Task.objects.all()
    }

    return render(request, "todo/index.html", context=context)
