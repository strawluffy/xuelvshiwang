from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import timezone
import datetime,time
from xuelvshiwang.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
import os


def hello(request):
	name='hello'
	local_time=timezone.now()
	return render_to_response('login/base.html',{'name':name,'local_time':local_time})
def index(request):
	endtime=time.mktime(datetime.datetime(2015,02,01,0,0).timetuple())
	now=time.time()
	delta=int(endtime-now)
	return render_to_response('login/index.html',{'delta':delta})
@csrf_exempt
def deploy(request):
	cmd_run=str(BASE_DIR)+"/sync_to_github.sh"
	os.system(cmd_run)

	return HttpResponse('hello,world')