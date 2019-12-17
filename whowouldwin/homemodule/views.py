from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home(request):

	context = settings.TEMPLATE_CONTEXT
	context['test_string'] = 'Howdy!'

	return render(request, 'templates/home.html', context)