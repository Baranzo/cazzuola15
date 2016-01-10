import json

from django.http import HttpResponse
from django.shortcuts import render

from scraper import get_doc_list


def index(request):

    return render(request, 'base.html')


def doc_list(request):

    data = get_doc_list()
    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')

