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

	primero = Voto.objects.filter(can=cand1).count()
	segundo = Voto.objects.filter(can=cand2).count()
	tercero = Voto.objects.filter(can=cand3).count()
	cuarto = Voto.objects.filter(can=cand4).count()
	total = primero+segundo+tercero+cuarto
	votos = [primero,segundo,tercero,cuarto]
	votos.sort()
	votos.reverse()

	res = list()
	porc = dict()
	a=True
	b=True
	c=True
	d=True
	for x in votos:
		if x == primero and a:
			a = False
			res.append(cand1)
			porc[cand1.nombre] = round((x*100.00)/total, 2)
		elif x == segundo and b:
			b = False
			res.append(cand2)
			porc[cand2.nombre] = round((x*100.00)/total, 2)
		elif x == tercero and c:
			c = False
			res.append(cand3)
			porc[cand3.nombre] = round((x*100.00)/total, 2)
		elif x == cuarto and d:
			d = False
			res.append(cand4)
			porc[cand4.nombre] = round((x*100.00)/total, 2)

	return render_to_response("resultados.html", 
		{'titulo':'- Resultados', 
		'cand1': res[0],
		'cand2': res[1],
		'cand3': res[2],
		'cand4': res[3],
		'votos1': porc[res[0].nombre],
		'votos2': porc[res[1].nombre],
		'votos3': porc[res[2].nombre],
		'votos4': porc[res[3].nombre],
		}, 
		context_instance=RequestContext(request));