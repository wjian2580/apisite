from django.shortcuts import render,get_object_or_404
from django.http import Http404

# Create your views here.

from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
	latest_five = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_five': latest_five
	}
	return render(request, 'polls/index.html', context)

def detail(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
	response = '正在查看问题的投票结果：%s' % question_id
	return HttpResponse(response)

def vote(request, question_id):
	return HttpResponse('正在给问题%s投票' % question_id) 

