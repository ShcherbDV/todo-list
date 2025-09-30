from django.urls import path

from todo_app.views import index, TagListView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_app"