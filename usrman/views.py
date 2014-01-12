from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.utils.http import urlquote
import string, random
from usrman.models import Pending
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

# TODO Handle bad requests, add success pages

# Create your views here.
def lin(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('usrman:test')
	else:
		form = AuthenticationForm
	return render(request, 'usrman/login.html', {'form': form})

def lout(request):
	logout(request)
	return HttpResponseRedirect(reverse('usrman:test'))

def new(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			if 'northwestern.edu' in username:
				password = form.cleaned_data['password1']
				user = User.objects.create_user(username, '', password)
				user.is_active = False
				user.save()
				code = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(25))
				p = Pending(user=user, string=code)
				p.save()
				send_mail(
					'Confirm',
					'localhost:8000/usrman/confirm/?usr=' + urlquote(user.username) + "&code=" + code,
					'from@example.com',
					[user.username],
					fail_silently=False)
				return HttpResponseRedirect(reverse('usrman:test'))
	else:
		form = UserCreationForm
	return render(request, 'usrman/newusr.html', {'form': form})

def confirm(request):
	if request.method == 'GET':
		username = request.GET['usr']
		code = request.GET['code']
		print username
		print code
		p = Pending.objects.get(user__username__exact=username)
		if p.string == code:
			p.user.is_active = True
			p.user.save()
			p.delete()
	return HttpResponseRedirect(reverse('usrman:test'))

@login_required(login_url='/usrman/login/')
def example(request):
	print request.user.plan
	return HttpResponse("Work dangit")