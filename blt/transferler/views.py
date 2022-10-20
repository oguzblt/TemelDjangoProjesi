from django.shortcuts import render
from django.shortcuts import get_object_or_404
from.models import transferTablo
# Create your views here.

def index(request):
    transfer = transferTablo.objects.all()
    icerik = {
        'transferler': transfer
    }
    return render(request, 'transferler/list.html', icerik)

def detail(request, transfer_id):
    haber = get_object_or_404(transferTablo, pk=transfer_id)
    context ={
        'transfer': haber
    }
    return render(request, 'transferler/detail.html', context)

def search(request):
    return render(request, 'transferler/search.html')

def transEkle(request):
    if request.method == 'POST':
        if not request.POST['adi'] or not request.POST['transferDetay']:
            pass
        else:
            s=transferTablo()
            s.adi = request.POST['adi']
            s.soyadi = request.POST['soyadi']
            s.transferDetay = request.POST['transferDetay']
            s.resim = request.POST['resim']

            s.save()
            return render(request,'transferler/transEkle.html')
    return render(request, 'transferler/transEkle.html',)

