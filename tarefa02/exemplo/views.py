from django.shortcuts import render

def index(request):
    print (request.method)
    print (request.META["HTTP_USER_AGENT"])
    print (f"Bem Vindo{ request.GET.get('nome')}")
    print (request.GET)
    return render(request, "index.html")
    
def outra(request):
    return render(request,"outra.html")

def terceira(request):
    return redirect('outra')