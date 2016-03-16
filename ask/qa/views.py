from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import Question

def ask_view(request):
  if request.method == 'POST':
    form = AskForm(request.POST)
    form.author = request.user
    if form.is_valid():
      question = Question.objects.create(author=form.author,
                                         title = form.cleaned_data['title'],
                                         text = form.cleaned_data['text'])
      url = question.get_url()
      return HttpResponseRedirect(url)
  else:
    form = AskForm(initial = {'author': request.user})
  return render(request, 'questions/ask_form.html', { 'form': form })

def answer_add(request):
  form = AnswerForm(request.POST)
  if form.is_valid():
    answer = form.save()
    url = answer.get_url()
    return HttpResponseRedirect(url)
  raise Http404

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
    if request.method == 'POST':
      return answer_add(request)
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    return render(request, 'questions/question_details.html', {
        'question': question,
        'answers': answers,
    })

def test(request, *args, **kwargs):
    #return HttpResponse('OK')
    return render(request,'index2.html')
def page404(request, *args, **kwargs):
    raise Http404

def question(request, id):
   return render(request,'index.html',{'id': id,})
