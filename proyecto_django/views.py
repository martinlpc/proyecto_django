from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def saludo(request):
  return HttpResponse("<b>Hola ChanDJANGO</b>")

def dia_de_hoy(request):
  dia = datetime.datetime.now()
  doc = f"Hoy es: <br> {dia}"

  return HttpResponse(doc)

def mi_nombre(self,nombre):
  doc = f"Mi nombre es: <br> {nombre}"

  return HttpResponse(doc)

def probando_template(self):
  nom = 'Martin'
  ape = 'Pacheco'
  my_dict = {'nombre':nom, 'apellido':ape}
  
  my_template = loader.get_template('template_1.html')

  doc = my_template.render()

  return HttpResponse(doc)