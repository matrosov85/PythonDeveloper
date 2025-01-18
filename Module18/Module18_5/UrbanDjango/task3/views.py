from django.shortcuts import render


def platform_view(request):
    return render(request, 'third_task/platform.html')


def games_view(request):
    context = {
        'games': [
            'Atomic Heart',
            'Cyberpunk 2077',
            'Pay Day 2'
        ]
    }
    return render(request, 'third_task/games.html', context=context)


def cart_view(request):
    return render(request, 'third_task/cart.html')
