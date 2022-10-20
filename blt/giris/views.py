from django.shortcuts import render

def ilksayfa(request):
    return render(request, 'giris/ilksayfa.html')
def ucuncusayfa(request):
    return render(request, 'giris/ucuncusayfa.html')


