from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import *
# Create your views here.

def index(request):

    booklist = BookInfo.objects.all()
    content = {'booklist': booklist, 'title': 'book'}
    # temp = loader.get_template('booktest/index.html')
    # req_context = RequestContext(request, {})
    # ret_html = temp.render(req_context)
    return render(request, 'booktest/index.html', content)

def detail(request,bid):
    book = BookInfo.objects.get(id=bid)

    herolist = book.heroinfo_set.all()

    return render(request, 'hero/heroinfo.html', {'herolist': herolist})