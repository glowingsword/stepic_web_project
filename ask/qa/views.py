from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.core.urlresolvers import reverse
from .models import Question
from .models import Answer
from .forms import AskForm
from .forms import AnswerForm
from .forms import SignUpForm
from .forms import LoginForm


def ask_view(request):
  if request.method == 'POST':
    form = AskForm(request.POST)
    #form.author = request.user
    if form.is_valid():
      ask = form.save()
      url = reverse('question_details', args=[ask.id])
      return HttpResponseRedirect(url)
  else:
    form = AskForm()
  return render(request, 'questions/ask_form.html', { 'form': form })

def answer_add(request):
  form = AnswerForm(request.POST)
  if form.is_valid():
    answer = form.save()
    url = reverse('question_detail', args=[answer.question.id])
    return HttpResponseRedirect(url)
  return HttpResponseRedirect('/')

def pagination(request,questions,baseurl):
  try:
    limit = int(request.GET.get('limit', 10))
  except ValueError:
    limit = 10
  if limit > 100:
    limit = 10
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    raise Http404
  paginator = Paginator(questions, limit)
  paginator.baseurl = baseurl
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)
  return (page,paginator)

def questions_list_all(request):
    questions = Question.objects.all()
    questions = Question.objects.order_by('-added_at')
    page,paginator=pagination(request,questions,'/?page=')
    return render(request, 'questions/new_questions.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def questions_list_popular(request):
    questions = Question.objects.all()
    questions = Question.objects.order_by('-rating')
    page,paginator=pagination(request,questions,'/popular/?page=')
    return render(request, 'questions/popular_questions.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def question_details(request, id):
    #if request.method == 'POST':
    #  return answer_add(request)
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    answer_form = AnswerForm(initial = {'question': question, 'author': request.user})
    return render(request, 'questions/question_details.html', {
        'question': question,
        'form': answer_form,
        'answers': answers,
    })

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            form.save()
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'questions/signup.html', {
        'form': form
    })

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'questions/login.html', {
        'form': form
    })

def test(request, *args, **kwargs):
    #return HttpResponse('OK')
    return render(request,'index2.html')
def page404(request, *args, **kwargs):
    raise Http404

def question(request, id):
   return render(request,'index.html',{'id': id,})
