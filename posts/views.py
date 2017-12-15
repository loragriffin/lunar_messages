from django.shortcuts import render

from .models import Post
from .form import PostForm


def home(request):
    queryset = Post.objects.all().order_by("-timestamp")
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = PostForm()

    context = {
        "form": form,
        "list": queryset
    }

    return render(request, "index.html", context)
