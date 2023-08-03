from django.shortcuts import render

def home(request):
    return render(request,'per_site.html')
