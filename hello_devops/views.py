from django.http import HttpResponse

def hello_index(request):
	return HttpResponse("Hello, World!")