from django.shortcuts import render


def platform_view(request):
    return render(request, 'platform.html')


def games_view(request):
    context = {
        'games': [
            'Atomic Heart',
            'Cyberpunk 2077',
            'Pay Day 2'
        ]
    }
    return render(request, 'games.html', context=context)


def cart_view(request):
    return render(request, 'cart.html')
