from django.http import HttpResponse, JsonResponse

def hello_world(request):
    return HttpResponse("<h1>Hello World!</h1>")

def health_check(request):
    return JsonResponse({"status": "ok"})
