from django.contrib import admin
from aset.models import *

# Register your models here.
class AsetAdmin (admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_aset']
    list_filter = ('jenis_aset',)
    search_fields = []
    list_per_page = 25

admin.site.register(Aset, AsetAdmin)

class IzinAdmin (admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_aset',  'disetujui']
    list_filter = ('jenis_aset', 'disetujui')
    search_fields = ['alasan']
    list_per_page = 25

    actions = ['setujui_izin', 'batalkan_izin']

    def setujui_izin(self, request, queryset):
    	for izin in queryset:
    	    izin.disetujui = True
    	    izin.save()

    setujui_izin.short_description = "Terima pengajuan izin yang dipilih"


    def batalkan_izin(self,request,queryset):
    	queryset.update(disetujui=False)

    batalkan_izin.short_description = "Batalkan pengajuan izin yang dipilih"

admin.site.register(Izin, IzinAdmin)