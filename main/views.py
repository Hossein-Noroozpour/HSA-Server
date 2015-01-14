from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from main.models import Agents


def index(request):
    return HttpResponse("Hello, world. You're at the main index. request is: " + str(request))


def register(request):
    return HttpResponse("Hello, world. You're at the main register. request is: " + str(request))


def show(request):
    agents_list = Agents.objects.order_by('last_name')
    template = loader.get_template('main/show.html')
    context = RequestContext(request, {'agents_list': agents_list, })
    return HttpResponse(template.render(context))