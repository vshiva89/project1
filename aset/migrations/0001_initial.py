# Generated by Django 2.0.1 on 2018-01-25 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_aset', models.CharField(choices=[('laptop', 'Laptop'), ('hp', 'HP')], max_length=20)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Karyawan')),
            ],
        ),
        migrations.CreateModel(
            name='Izin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_aset', models.CharField(choices=[('laptop', 'Laptop'), ('hp', 'HP')], max_length=20)),
                ('alasan', models.TextField()),
                ('disetujui', models.BooleanField(default=False)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Karyawan')),
            ],
        ),
    ]
