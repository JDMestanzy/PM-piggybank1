from django.shortcuts import render

from django.http import HttpResponse


def indexPageView(request):
    return HttpResponse('This is the piggy app yallll!'
                        )
