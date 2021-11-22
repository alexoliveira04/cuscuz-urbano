from django.http import HttpResponse


def index(request):
    return HttpResponse('Olá mundo, essa é uma resposta HTTP')