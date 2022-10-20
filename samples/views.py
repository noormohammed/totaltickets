from django.http import HttpResponse
from samples.sample_function import  do_lots_of_things
from django.views import View


class SamplesView(View):

    def index(request):
        answer = do_lots_of_things(
            999, '123.231', '2023-10-22 11:55:12'
        )
        return HttpResponse(
            f'Result of do_lots_of_things is: <strong>{answer}</strong>'
        )
