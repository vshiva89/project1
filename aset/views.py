from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from karyawan.models import Karyawan
from aset.models import Aset, Izin
from aset.forms import IzinForm

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors


# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def pengajuan_izin(request):
    if request.method == 'POST':
        form_data = request.POST
        form = IzinForm(form_data)
        if form.is_valid():
            izin = Izin(
                    karyawan = Karyawan.objects.get(id=request.session['karyawan_id']),
                    jenis_aset = request.POST['jenis_aset'],
                    alasan = request.POST['alasan'],
                    disetujui = False,
                )
            izin.save()
            return redirect('/')
    else:
        form = IzinForm()

    return render(request, 'tambah_izin.html', {'form':form})

@login_required(login_url=settings.LOGIN_URL)
def daftar_izin(request):
    daftar_izin = Izin.objects.filter(karyawan__id=request.session['karyawan_id'])
    return render(request, 'daftar_izin.html', {'daftar_izin':daftar_izin})


