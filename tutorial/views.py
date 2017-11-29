from django.shortcuts import render


def login_redirect(request):
    return render(request, 'account/main_page.html')