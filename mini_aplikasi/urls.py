from django.conf.urls import url
from django.contrib import admin

from homepage import views as homepage_views
from karyawan import views as karyawan_views
from aset import views as aset_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', karyawan_views.profil),
    url(r'^login/', homepage_views.login_view),
    url(r'^logout/', homepage_views.logout_view),
    url(r'^pengajuan_izin/', aset_views.pengajuan_izin),
    url(r'^daftar_izin/', aset_views.daftar_izin),
]
