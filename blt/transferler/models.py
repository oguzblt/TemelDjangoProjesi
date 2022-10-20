from django.db import models

# Create your models here.

class transferTablo(models.Model):
    adi = models.CharField(max_length=40)
    soyadi = models.CharField(max_length=40)
    transferDetay = models.TextField()
    resim = models.CharField(max_length=50)
    yuklemeTarih = models.DateTimeField(auto_now_add=True)
    yayınlanmaDurum = models.BooleanField(default=True)

    def __str__(self):
        return self.adi
    def get_resim_path(self):
        return '/img/' + self.resim


