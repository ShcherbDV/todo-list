from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import Tag, Task


def index(request):

    queryset = Task.objects.all().order_by("is_done", "-datetime")

    context = {
        "task_list": queryset,
    }

    return render(request, "todo_app/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get(
            "HTTP_REFERER", reverse_lazy("todo_app:tag-list")
        )
        return context


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get(
            "HTTP_REFERER", reverse_lazy("todo_app:tag-list")
        )
        return context


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get(
            "HTTP_REFERER", reverse_lazy("todo_app:tag-list")
        )
        return context


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get(
            "HTTP_REFERER", reverse_lazy("todo_app:index")
        )
        return context


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get(
            "HTTP_REFERER", reverse_lazy("todo_app:index")
        )
        return context


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get(
            "HTTP_REFERER", reverse_lazy("todo_app:index")
        )
        return context

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo_app:index"))