import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from models import Document
from scraper import get_doc_list, get_doc_body


@csrf_protect
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


@csrf_protect
def doc_request(request):

    doc_url = request.POST['url']

    doc_body = get_doc_body(doc_url)
    doc_body = json.dumps(doc_body)

    return HttpResponse(doc_body, content_type='text/html')
