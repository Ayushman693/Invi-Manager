from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from . forms import LoginForm


def home(request):
	return render(request, 'home.html')

def admin_home(request):
	return render(request, 'admin_login_home.html')

def login_base(request):
	return render(request, 'user_login_home.html')

@require_http_methods(['GET', 'POST'])
def main_login(request):
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('login_base')
			else:
				return redirect('login')

	kwargs = locals()
	return render(request, "login.html", kwargs)


def main_logout(request):
	logout(request)
	messages.add_message(request, messages.SUCCESS, 'Successfully logout')

	return redirect('home')