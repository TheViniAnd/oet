from django.shortcuts import render

def home_list(request):
    return render(request, 'home/home_list.html',{})