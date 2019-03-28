
from booking.Classes.UserManager import UserManager
from django.shortcuts import render
from booking.forms import RegisterForm
from django.http import HttpResponseRedirect

def register(request):
    userManager = UserManager()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            login = form.cleaned_data['login']
            password = form.cleaned_data['password']

            if 'login' in request.POST:
                for user in userManager.allUsers():
                    if user.name == login  and user.password == password:
                        return HttpResponseRedirect('/mainpage/')

            return HttpResponseRedirect('')

    else:
        form = RegisterForm()
        return render(request, 'booking/RegisterPage.html', {'form': form})

def main_page(request):
    return render(request, 'booking/MainPage.html')
