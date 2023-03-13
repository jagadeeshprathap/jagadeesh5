from django.shortcuts import render

# Create your views here.
def prathap(request):
    return render(request,"jaga.html",context={'name':'jagadeesh'})