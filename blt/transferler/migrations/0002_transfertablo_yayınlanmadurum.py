# Generated by Django 3.1.5 on 2021-02-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfertablo',
            name='yayınlanmaDurum',
            field=models.BooleanField(default=True),
        ),
    ]
