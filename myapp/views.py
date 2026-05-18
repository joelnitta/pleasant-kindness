import os
import markdown2
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    md_path = os.path.join(
        settings.BASE_DIR, "myapp", "content", "index.md"
    )
    with open(md_path, "r", encoding="utf-8") as f:
        content = markdown2.markdown(f.read())
    return render(request, "index.html", {"content": content})


def health_check(request):
    return JsonResponse({"status": "ok"})
