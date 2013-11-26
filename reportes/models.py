from django.db import models
from django.core.files import File

class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
		return self.nombre

class Alumno(models.Model):
    materia = models.ForeignKey(Materia)
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='files/', null=True, blank=True)

    def __unicode__(self):
		return self.nombre