from django.shortcuts import render_to_response
from django.utils import timezone
import datetime,time
def hello(request):
	name='hello'
	local_time=timezone.now()
	return render_to_response('login/base.html',{'name':name,'local_time':local_time})
def index(request):
	endtime=time.mktime(datetime.datetime(2014,12,01,0,0).timetuple())
	now=time.time()
	delta=int(endtime-now)
	return render_to_response('login/index.html',{'delta':delta})