# Generated by Django 4.0 on 2022-01-03 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nmap', '0002_delete_nmapresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='NmapResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.TextField()),
                ('ports', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
