from django.shortcuts import render

# Create your views here.
def jaga(request):
    return render(request,"jaga.html",context={'name':'narendra','age':21})