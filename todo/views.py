from django.shortcuts import render
from django.urls import reverse_lazy
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


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_confirm_delete.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_form.html"
