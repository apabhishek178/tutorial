from django.shortcuts import render
from django.shortcuts import redirect


def login_redirect(request):
    return render(request, 'account/main_page.html')

def controls(request):
    if request.method == 'POST':
        return redirect('/account/')

    else:
        return render(request, 'account/controls.html')
