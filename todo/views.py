from django.shortcuts import render
from django.views import generic

from todo.models import Task, Tag


def index(request):
    context = {
        "tasks": Task.objects.all()
    }

    return render(request, "todo/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
