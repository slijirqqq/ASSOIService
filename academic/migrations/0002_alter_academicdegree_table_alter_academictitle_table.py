# Generated by Django 4.1.1 on 2022-10-13 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='academicdegree',
            table='AcademicDegree',
        ),
        migrations.AlterModelTable(
            name='academictitle',
            table='AcademicTitle',
        ),
    ]
