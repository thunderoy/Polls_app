from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the INDEX page.")

def detail(request, question_id):
	return HttpResponse("This is the DETAIL page of question %s." % question_id)

def results(request, question_id):
	return HttpResponse("This is the RESULTS page of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("This is the VOTE page of question %s." % question_id)
