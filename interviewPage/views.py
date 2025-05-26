from django.shortcuts import render
from django.http import HttpResponse

def interview(request):
    return render(request, 'interviewPage/interviewPage.html')

# Create your views here.
