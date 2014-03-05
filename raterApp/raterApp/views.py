from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User
from django.template import RequestContext
from models import *

def home(request):
	allRatings = Rating.objects.select_related().all()
	return render_to_response('raterApp/index.html', {'ratings':allRatings}, context_instance=RequestContext(request))
