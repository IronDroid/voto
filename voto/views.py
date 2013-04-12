from django.shortcuts import render_to_response
from django.template import RequestContext
from voto.models import *

def index(request):
	return render_to_response("votoindex.html", context_instance=RequestContext(request));

def result(request):
	cand = Candidato.objects.get(id_candidato=1)
	primero = Voto.objects.filter(can=cand);
	cand = Candidato.objects.get(id_candidato=2)
	segundo = Voto.objects.filter(can=cand);
	cand = Candidato.objects.get(id_candidato=3)
	tercero = Voto.objects.filter(can=cand);
	cand = Candidato.objects.get(id_candidato=4)
	cuarto = Voto.objects.filter(can=cand);
	return render_to_response("resultados.html", 
		{'titulo':'- Resultados', 'primero': primero.count(), 'segundo': segundo.count(),
		 'tercero': tercero.count(), 'cuarto': cuarto.count()}, 
		context_instance=RequestContext(request));