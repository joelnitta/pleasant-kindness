import os

import markdown2
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render


def index(request):
    md_path = os.path.join(
        settings.BASE_DIR, "myapp", "content", "index.md"
    )
    with open(md_path, "r", encoding="utf-8") as f:
        content = markdown2.markdown(f.read())
    return render(request, "index.html", {"content": content})


def about(request):
    md_path = os.path.join(
        settings.BASE_DIR, "myapp", "content", "about.md"
    )
    with open(md_path, "r", encoding="utf-8") as f:
        content = markdown2.markdown(f.read())
    return render(request, "about.html", {"content": content})


def health_check(request):
    return JsonResponse({"status": "ok"})


@login_required
def members(request):
    return render(request, "members.html")


@login_required
def staff_dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Staff access required.")
    return render(request, "staff_dashboard.html")
