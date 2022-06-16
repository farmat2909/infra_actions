from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World!')


def second_page(request):
    return HttpResponse('А это вторая страница')
