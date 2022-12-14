# Generated by Django 3.1.5 on 2021-01-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transferler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resim', models.CharField(blank=True, max_length=50, verbose_name='resmi')),
                ('adi', models.CharField(max_length=50, verbose_name='adı')),
                ('soyadi', models.CharField(max_length=50, verbose_name='soyadı')),
                ('dtarih', models.DateTimeField(verbose_name='dogumtarihi')),
                ('uyruk', models.CharField(max_length=50, verbose_name='ülkesi')),
                ('nereden', models.CharField(max_length=50, verbose_name='nereden')),
                ('nereye', models.CharField(max_length=50, verbose_name='nereye')),
                ('durum', models.CharField(max_length=50, verbose_name='durumu')),
                ('bonservis', models.CharField(blank=True, max_length=20, verbose_name='bonservis')),
            ],
        ),
    ]
