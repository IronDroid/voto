from django.db import models

class Candidato(models.Model):
	id_candidato = models.SmallIntegerField(primary_key=True)
	nombre = models.TextField()
	partido = models.TextField()
	descripcion = models.TextField()
	def __unicode__(self):
		return self.nombre

class Voto(models.Model):
	can = models.ForeignKey(Candidato)
	fecha = models.DateField(auto_now=True)