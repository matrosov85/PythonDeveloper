from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f"Приветствуем, {username}!")

        if password != repeat_password:
            info['error1'] = 'Пароли не совпадают'
        if age < 18:
            info['error2'] = 'Вы должны быть старше 18'
        if username in users:
            info['error3'] = 'Пользователь уже существует'

    context = {
        'info': info
    }
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if password == repeat_password and age >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")

            if password != repeat_password:
                info['error1'] = 'Пароли не совпадают'
            if age < 18:
                info['error2'] = 'Вы должны быть старше 18'
            if username in users:
                info['error3'] = 'Пользователь уже существует'
        else:
            form = UserRegister()

    context = {
        'info': info,
        'form': form,
    }
    return render(request, 'registration_page.html', context)
