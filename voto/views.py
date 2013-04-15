from django.shortcuts import render_to_response
from django.template import RequestContext
from voto.models import *

def index(request):
	return render_to_response("votoindex.html", context_instance=RequestContext(request));

def result(request):
	cand1 = Candidato.objects.get(id_candidato=1)
	cand2 = Candidato.objects.get(id_candidato=2)
	cand3 = Candidato.objects.get(id_candidato=3)
	cand4 = Candidato.objects.get(id_candidato=4)
	candidatos = [cand1,cand2,cand3,cand4]
	primero = Voto.objects.filter(can=cand1).count();
	segundo = Voto.objects.filter(can=cand2).count();
	tercero = Voto.objects.filter(can=cand3).count();
	cuarto = Voto.objects.filter(can=cand4).count();
	votos = [primero,segundo,tercero,cuarto]
	votos.sort()
	votos.reverse()
	
	total = primero+segundo+tercero+cuarto

	return render_to_response("resultados.html", 
		{'titulo':'- Resultados', 
		'primero': round((primero*100.00)/total, 2), 
		'segundo': round((segundo*100.00)/total, 2), 
		'tercero': round((tercero*100.00)/total, 2), 
		'cuarto': round((cuarto*100.00)/total, 2), 
		'cand1': cand1.nombre, 
		'cand2': cand2.nombre, 
		'cand3': cand3.nombre, 
		'cand4': cand4.nombre}, 
		context_instance=RequestContext(request));