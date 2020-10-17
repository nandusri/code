from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('dashboard')
	else:
		form = UserCreationForm()			
	context = {'form' : form}
	return render(request, 'register.html', context)


@login_required
def dashboard(request):
	if request.user.is_superuser:
		user = User.objects.exclude(username=request.user)
		return render(request, 'dashboard.html',{'users':user})
	else:
		user = User.objects.filter(username=request.user)
		return render(request, 'dashboard.html',{'users':user})

