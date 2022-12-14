# Generated by Django 4.1.1 on 2022-10-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('academic', '0001_initial'), ('academic', '0002_alter_academicdegree_table_alter_academictitle_table')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted?')),
                ('date', models.DateField(verbose_name='Date')),
                ('diploma_number', models.CharField(max_length=13, verbose_name='Diploma number')),
                ('name', models.CharField(choices=[('technic_phd', 'Technic PhD'), ('chemistry_phd', 'Chemistry PhD'), ('candidate_of_pedagogical_sciences', 'Pedagogical PhD'), ('candidate_of_physical_mathematical_sciences', 'Physical and Mathematical PhD'), ('doctor_of_technical_sciences', 'Doctor of Technical Sciences'), ('doctor_of_chemistry_sciences', 'Doctor of Chemistry Sciences'), ('doctor_of_pedagogical_sciences', 'Doctor of Pedagogical Sciences'), ('doctor_og_physic_and_math_sciences', 'Doctor of Physical and Mathematical Sciences')], max_length=128, verbose_name='Academic degree')),
            ],
            options={
                'verbose_name': 'Academic degree',
                'verbose_name_plural': 'Academic degrees',
            },
        ),
        migrations.CreateModel(
            name='AcademicTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted?')),
                ('date', models.DateField(verbose_name='Date')),
                ('diploma_number', models.CharField(max_length=13, verbose_name='Diploma number')),
                ('name', models.CharField(choices=[('professor', 'Professor'), ('docent', 'Docent'), ('scientist', 'Scientist employee'), ('high_scientist', 'High scientist employee')], max_length=128, verbose_name='Academic title')),
            ],
            options={
                'verbose_name': 'Academic title',
                'verbose_name_plural': 'Academic titles',
            },
        ),
        migrations.AlterModelTable(
            name='academicdegree',
            table='AcademicDegree',
        ),
        migrations.AlterModelTable(
            name='academictitle',
            table='AcademicTitle',
        ),
    ]
