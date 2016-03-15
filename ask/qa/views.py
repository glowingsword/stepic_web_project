from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from .models import Question

def pagination(request,baseurl):
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
    page,paginator=pagination(request,'/?page=')
    return render(request, 'questions/new_questions.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def questions_list_popular(request):
    questions = Question.objects.all()
    questions = Question.objects.order_by('-rating')
    page,paginator=pagination(request,'/popular/?page=')
    return render(request, 'questions/popular_questions.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answers.all()
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
