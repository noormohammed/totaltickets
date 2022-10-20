# from django.shortcuts import render
from datetime import datetime
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from samples.sample_function import  do_lots_of_things
from django.conf import settings


def index(request):
    answer = do_lots_of_things(
        999,
        '123.231',
        '2021-10-22'
    )
    return HttpResponse(
        f'Result of do_lots_of_things is: <strong>{answer}</strong>'
    )
