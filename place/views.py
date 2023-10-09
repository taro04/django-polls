from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, Http404,  HttpResponseRedirect
from .models import Idea
from django.views import generic
from django.utils import timezone
# Create your views here.


class DetailView(generic.DetailView):
    model = Idea
    template_name = 'place/detail.html'


def detail(request, question_id):
    # try:
    # q = Question.objects.get(pk=question_id)
    q = get_object_or_404(Idea, pk=question_id)
    # except:
    #    raise Http404("Q dose not ex")
    return HttpResponse("You're looking at question %s." % question_id)
    # return render(request, "polls/detail.html", {"question":q})


def index(request):
    # sample code from https://chigusa-web.com/blog/django-leaflet/
    # template = loader.get_template('place/index.html')
    # return HttpResponse(template.render(None, request))
    g = timezone.datetime.now()
    return render(request, "place/index.html", {"g": g})


def index2(request):
    # a=
    pass
