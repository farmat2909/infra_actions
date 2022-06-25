from django.http import HttpResponse


def index(request):
    return HttpResponse('Я запустил сервер!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
