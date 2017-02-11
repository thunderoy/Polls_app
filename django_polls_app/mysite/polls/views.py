from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

def index(request):
	latest_questions = Question.objects.order_by('-publish_date')[::-1]
	return render(request, 'polls/index.html', {'latest_questions': latest_questions})

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except:
		return render(request, 'polls/detail.html', {'question': question,
			'error_message': "Please select an option"})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return redirect('polls:results', question_id=question_id)