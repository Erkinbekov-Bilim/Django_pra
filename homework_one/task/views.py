from django.shortcuts import render, HttpResponse

# Create your views here.


def get_response(request):
    return HttpResponse("Task one")

def task_view(request):
    return render(request, 'main.html')