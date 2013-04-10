from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from voto.models import *

@dajaxice_register
def recibir_votos(request, num_can):
	candidato = Candidato.objects.get(id_candidato=num_can)
	voto = Voto(can=candidato)
	voto.save()
	return simplejson.dumps({'mensaje': candidato.nombre})
