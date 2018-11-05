from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.adopcion.forms import PersonaForm

# Create your views here.

def index(request):
	return render(request, 'Persona/index.html')


def adopcion_view(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = PersonaForm()

	return render(request, 'Persona/persona_form.html', {'form':form})