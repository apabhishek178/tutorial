from django.shortcuts import render


def login_redirect(request):
    return render(request, 'account/main_page.html')

def controls(request):
    return render(request, 'account/controls.html')
