from django.contrib import admin
from.models import transferTablo

class transferAdmin(admin.ModelAdmin):
    list_display = ('adi', 'soyadi', 'yuklemeTarih', 'yayınlanmaDurum')
    list_display_links = ('adi', 'soyadi')
    list_filter = ('adi', 'yuklemeTarih')
    list_editable = ('yayınlanmaDurum',)
    search_fields = ('adi', 'soyadi')
    list_per_page = 10

# Register your models here.
admin.site.register(transferTablo, transferAdmin)
