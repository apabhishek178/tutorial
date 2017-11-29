from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
    name = "Abhishek"
    branch = "Information Technology"
    college = "College of Engineering Roorkee "
    num = [1, 2, 3, 4]
    args = {"name": name, "college": college, "branch": branch, "year": num}
    return render(request, 'account/home.html', args)


def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        form.save()
        return redirect('/account')
    else:
        form = RegistrationForm()

        args={'form':form}
        return render(request, 'account/reg_form.html', args)


def profile(request):
    args = {'user':request.user}
    return render(request, 'account/profile.html', args)


def edit_profile(request):
    if request.method =='POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form':form}
        return render(request, "account/edit_profile.html", args)




