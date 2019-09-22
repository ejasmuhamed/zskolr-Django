from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('dashboard')
		else:
			error = True
			return render(request, 'accounts/login.html', {'error': error})
	else:
		if request.user.is_active:
			auth.logout(request)
		return render(request, 'accounts/login.html')

@login_required
def logout(request):
	auth.logout(request)
	return redirect('dashboard')
	#return render(request, 'accounts/login.html')



def signup(request):
	return render(request, 'accounts/signup.html')