from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse("Hello, World!")


def say_hello_html(request):
    return render(request, "playground/hello.html", {'name': '3반', 'greeting': '반갑다'})


def say_bye(request):
    context = {
        'name': '김지훈 선생님',
        'bye': '안녕히'
    }
    return render(request, "playground/bye.html", context=context)
