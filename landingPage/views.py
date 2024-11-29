from django.shortcuts import render

def explore(request):
    return render(request , 'landing_page/explore.html')
