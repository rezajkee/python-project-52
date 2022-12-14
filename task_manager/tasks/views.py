from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django_filters.views import FilterView

from ..utils import CustomLoginRequiredMixin, TasksUserPassesTestMixin
from .filters import TaskFilter
from .forms import TaskCreationForm
from .models import Task


class TaskCreateView(
    CustomLoginRequiredMixin, SuccessMessageMixin, generic.CreateView
):
    """Task creation only by a logged-in user
    with adding this user as the author and
    adding the success message."""

    form_class = TaskCreationForm
    success_url = reverse_lazy("tasks")
    template_name = "tasks/create_task.html"
    success_message = _("The task was created successfully")

    def form_valid(self, form):
        # Add logged-in user as the author
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskListView(CustomLoginRequiredMixin, FilterView):
    """Rendering a list of all existing tasks only by a logged-in user.
    With adding a custom filtering by a FilterView and TaskFilter."""

    model = Task
    fields = ("id", "name", "creation_date")
    context_object_name = "all_tasks"
    ordering = ["creation_date"]
    template_name = "tasks/tasks.html"
    filterset_class = TaskFilter


class TaskUpdateView(
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    """Updating task's fields only by a logged-in user
    with adding the success message."""

    model = Task
    form_class = TaskCreationForm
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy("tasks")
    success_message = _("The task was edited successfully")


class TaskDeleteView(
    CustomLoginRequiredMixin,
    TasksUserPassesTestMixin,
    SuccessMessageMixin,
    generic.DeleteView,
):
    """Deleting a task only by the author
    with adding the success message."""

    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("tasks")
    success_message = _("The task was deleted successfully")

    def test_func(self):
        author = Task.objects.get(id=self.kwargs["pk"]).author
        return self.request.user == author


class TaskDetailView(
    CustomLoginRequiredMixin,
    generic.DetailView,
):
    """Rendering a page of the detailed task only by a logged-in user."""

    model = Task
    template_name = "tasks/detail_task.html"
