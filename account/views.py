from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import LoginForm


class LoginForm(View):
    def get(self, request):
        form = LoginForm()
        return  render(request, 'account/Login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Success")
            else:
                return HttpResponse("Disabled account")
        else:
            return HttpResponse('Invalid login')
        return render(request, 'account/Login.html', {'form': form})