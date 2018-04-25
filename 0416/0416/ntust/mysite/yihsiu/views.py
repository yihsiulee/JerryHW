from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Myid
# Create your views here.
def index(request):
	myid=Myid.objects.all()
	return render_to_response('yihsiu/profiles.html',locals())
