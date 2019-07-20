from django.shortcuts import render, redirect
from apps.login_app.models import *
from django.contrib import messages

def login_page(request):
    request.session['user_first_name'] = ''
    return render(request, "login_app/login_page.html")

def action_register(request):
    errors = User.objects.basic_validator_register(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(first_name=request.POST["input_first_name"], last_name=request.POST["input_last_name"],
        email=request.POST["input_email"], password=request.POST["input_password"])

        request.session['user_first_name'] = user.first_name

        return redirect('/success')

def action_login(request):
    errors = User.objects.basic_validator_login(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        matching_users_list = User.objects.filter(email=request.POST["input_email"],
                                                  password=request.POST["input_password"])
        if len(matching_users_list) != 0:
            request.session['user_first_name'] = matching_users_list[0].first_name
        else:
            return redirect('/')
        return redirect('/success')

def success_page(request):
    if request.session['user_first_name'] != '':
        return render(request, "login_app/success.html",)
    else:
        return redirect('/')