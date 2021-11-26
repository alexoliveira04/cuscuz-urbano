from django.http import HttpResponseRedirect, HttpResponse 
from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Retorne as últimas cinco questões publicadas."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

def vote(request, question_id):
    ... # O mesmo que acima, nenhuma mudança necessária.

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Exiba novamente o formulário de votação da pergunta.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Você não selecionou uma escolha.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Sempre retorna um HttpResponseRedirect após lidar com sucesso
        # com dados POST. Isso evita que os dados sejam postados duas vezes se um
        # usuário clica no botão Voltar.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))










'''def index(request):
    return HttpResponse('Olá mundo')

def detail(request, question_id):
    return HttpResponse("Você está olhando para uma questão %s." % question_id)

def results(request, question_id):
    response = "Você está olhando para os resultados da pergunta %s."
    return HttpResponse(response % question_id)

    def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})'''