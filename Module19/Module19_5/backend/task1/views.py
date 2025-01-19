from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game, News


def platform_view(request):
    return render(request, 'platform.html')


def games_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games.html', context=context)


def cart_view(request):
    return render(request, 'cart.html')


def news_view(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': page_obj
    }
    return render(request, 'news.html', context=context)


def sign_up_by_html(request):
    info = {}
    users = list(Buyer.objects.values_list('name', flat=True))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password == repeat_password and age >= 18 and username not in users:
            Buyer.objects.create(name=username, balance=0, age=age)
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
    users = list(Buyer.objects.values_list('name', flat=True))
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
                Buyer.objects.create(name=username, balance=0, age=age)
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
