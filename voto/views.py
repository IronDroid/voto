from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response("votoindex.html", context_instance=RequestContext(request));

def result(request):
	return render_to_response("resultados.html", {'titulo':'Resultados'}, context_instance=RequestContext(request));