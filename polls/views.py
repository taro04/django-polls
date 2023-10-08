from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, Http404,  HttpResponseRedirect
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    #try:
        #q = Question.objects.get(pk=question_id)
    q = get_object_or_404(Question, pk=question_id)
    #except:
    #    raise Http404("Q dose not ex")
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, "polls/detail.html", {"question":q})

def results(request, question_id):
    response = "You are looking at the results of question %s"
    #return HttpResponse(response % question_id )
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    # return HttpResponse("you are voting on question %s." % questions_id )

    q = get_object_or_404(Question, pk=question_id)
    try:
        sss = request.POST['choice']
        print("sss--",sss)
        selected_choice = q.choice_set.get(pk=sss)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))