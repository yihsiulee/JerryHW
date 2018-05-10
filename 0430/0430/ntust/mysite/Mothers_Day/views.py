from django.shortcuts import render

from .models import *

def mom(request):
	q=''
	if request.method=='POST':
		q=request.POST.get('q')
		Mom.objects.create(q=q)
	return render(request,'Mothers_Day/mom.html',{'q':q})

# Create your views here.
#def search_form(request):
#	return render_to_response('Mothers_Day/search_form.html')

#def search(request):
#	request.encoding='utf-8'
#	message='你填入的內容為: '+request.GET['q']
#	return HttpResponse(message)

#def index(request):
	#return HttpResponse("aaa")
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	output = ','.join([q.question_text for q in latest_question_list])
#	return HttpResponse(output)

#def detail(request,question_id):
#	return HttpResponse("you are looking at question %s." %question_id)

#def results(request,question_id):
#	response = "you are looking at the results of question %s."
#	return HttpResponse(response % question_id)

#def vote(request,question_id):
#	return HttpResponse("you are voting on question %s." %question_id)