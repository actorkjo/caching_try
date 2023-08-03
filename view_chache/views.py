from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache


# per view caching:
@cache_page(60)
def home1(request):
    return render(request, 'per_view.html')


# template fragement caching:
def home2(request):
    return render(request, 'per_view.html')


# low level caching of API:
def home3(request):
    foo = cache.get('movie', 'nothing')
    if foo == 'nothing':
        cache.set('movie', 'baipan bhari', 120)
        foo = cache.get('movie')
    return render(request, 'home3.html', {'foo': foo})
