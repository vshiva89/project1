from django.forms import ModelForm
from django import forms
from aset.models import Izin

class IzinForm(ModelForm):
    class Meta:
        model = Izin
        fields = ['jenis_aset', 'alasan']
        labels = {
            'jenis_aset':"Jenis Aset",
            'alasan':'Alasan',
        }
        error_messages = {
            'jenis_aset': {
                'required': 'Anda harus memilih jenis aset'
            },
        
            'alasan':{
                'required': "Alasan harus diisi agar dapat disetujui oleh Manager"
            }
        }
        widgets = {
            'alasan': forms.Textarea(attrs={ 'cols':50, 'rows': 10 })
        }