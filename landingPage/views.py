from django.shortcuts import render

def explore(request):
    return render(request , 'landing_page/landing_page.html')
