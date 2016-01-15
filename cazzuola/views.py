import json

from django.http import HttpResponse
from django.shortcuts import render

from models import Document
from scraper import get_doc_list


def index(request):

    return render(request, 'base.html')


def doc_list(request):

    '''
    data ha la struttura
    {
        url: '',
        title: ''
    }
    '''

    d_list = Document.objects.all()
    data = []

    if not d_list:

        data = get_doc_list()

        for article in data:
            d = Document(title=article['title'], url=article['url'])
            d.save()

    else:
        for doc in d_list:
            data.append({'title': doc.title, 'url': doc.url})

    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')


def doc_request(request):

    doc_url = request.POST.keys()[0]

    #return HttpResponse(doc_body
