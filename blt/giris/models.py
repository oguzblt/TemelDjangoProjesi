from django.db import models

#Create your models here.

class iptal(models.Model):
    id = models.AutoField(primary_key=True)
    resim = models.CharField("resmi", max_length=50, blank=True)
    adi = models.CharField("adı", max_length=50)
    soyadi = models.CharField("soyadı", max_length=50)
    dtarih = models.DateTimeField("dogumtarihi")
    uyruk = models.CharField("ülkesi", max_length=50)
    nereden = models.CharField("nereden", max_length=50)
    nereye = models.CharField("nereye", max_length=50)
    durum = models.CharField("durumu", max_length=50)
    bonservis = models.CharField("bonservis", max_length=20, blank=True)

    def __str__(self):
        return self.adi+""+self.soyadi


