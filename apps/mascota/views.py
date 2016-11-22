from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

#from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota



def index(request):
	return render (request,'mascota/index.html')


def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm (request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:index')
	else:
		form = MascotaForm()


	return render(request, 'mascota/mascota_form.html', {'form':form})