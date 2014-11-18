from django.shortcuts import render_to_response

def hello(request):
	name='hello'
	return render_to_response('login/base.html',{'name':name})
def index(request):
	return render_to_response('login/index.html')