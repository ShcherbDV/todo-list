from django.shortcuts import render
from django.views import generic

from todo_app.models import Tag, Task


def index(request):

    queryset = Task.objects.all().order_by("is_done").order_by("datetime")


    context = {
        "task_list": queryset,
    }

    return render(request, "todo_app/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag