from __future__ import unicode_literals

from django.db import models
from karyawan.models import Karyawan

# Create your models here.
class Aset(models.Model):
    JENIS_ASET_CHOICES = (
        ('laptop', 'Laptop'),
        ('hp', 'HP'),
    )

    karyawan = models.ForeignKey(Karyawan,
    on_delete=models.CASCADE,)
    jenis_aset = models.CharField(max_length=20, choices=JENIS_ASET_CHOICES)
    #waktu = models.DateField()

    def __str__(self):
        return self.karyawan.nama

class Izin(models.Model):
    JENIS_ASET_CHOICES = (
        ('laptop', 'Laptop'),
        ('hp', 'HP')
    )

    karyawan = models.ForeignKey(Karyawan,
    on_delete=models.CASCADE,)
    jenis_aset = models.CharField(max_length=20, choices=JENIS_ASET_CHOICES)
    #waktu_mulai = models.DateField()
    #waktu_berhenti = models.DateField()
    alasan = models.TextField()
    disetujui = models.BooleanField(default=False)

    def __str__(self):
        return self.karyawan.nama
