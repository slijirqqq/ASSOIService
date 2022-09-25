# Generated by Django 4.1.1 on 2022-09-25 00:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=256, unique=True, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=14, null=True, region=None, verbose_name='Phone number')),
                ('first_name', models.CharField(max_length=128, verbose_name='First name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last name')),
                ('middle_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Middle name')),
                ('photo', models.ImageField(blank=True, default='images/default.png', upload_to='media/images', verbose_name='Avatar')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('education_level', models.CharField(blank=True, choices=[('high_education', 'High education'), ('college_tech_education', 'College tech education'), ('college_education', 'College education')], max_length=128, null=True, verbose_name='Education level')),
                ('stake', models.CharField(blank=True, choices=[('staff', 'Staff'), ('internal', 'Internal part-time worker'), ('external', 'External part-time worker')], max_length=128, null=True, verbose_name='Stake')),
                ('total_work_experience', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Total work experience')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['id', 'first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='ProfessionalDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted?')),
                ('date', models.DateField(verbose_name='Date of advanced training')),
                ('position', models.CharField(max_length=256, verbose_name='Place of advanced training')),
                ('hours_count', models.PositiveSmallIntegerField(verbose_name='Number of hours')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupportTeachingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(choices=[('engineer', 'Engineer'), ('high_engineer', 'High engineer'), ('lead_engineer', 'Lead engineer'), ('first_category_technician', 'Laboratory assistant of the 1st category'), ('laboratory_head', 'Head laboratory'), ('first_category_technic', 'Technician 1st category')], max_length=128, verbose_name='Post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sts_users', to=settings.AUTH_USER_MODEL, verbose_name='std_user')),
            ],
            options={
                'verbose_name': 'STS',
                'verbose_name_plural': 'STS employee',
            },
        ),
        migrations.CreateModel(
            name='PTeachingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_degree', models.CharField(choices=[('technic_phd', 'Technic PhD'), ('chemistry_phd', 'Chemistry PhD'), ('candidate_of_pedagogical_sciences', 'Pedagogical PhD'), ('candidate_of_physical_mathematical_sciences', 'Physical and Mathematical PhD'), ('doctor_of_technical_sciences', 'Doctor of Technical Sciences'), ('doctor_of_chemistry_sciences', 'Doctor of Chemistry Sciences'), ('doctor_of_pedagogical_sciences', 'Doctor of Pedagogical Sciences'), ('doctor_og_physic_and_math_sciences', 'Doctor of Physical and Mathematical Sciences')], max_length=128, verbose_name='Academic degree')),
                ('academic_title', models.CharField(choices=[('professor', 'Professor'), ('docent', 'Docent'), ('scientist', 'Scientist employee'), ('high_scientist', 'High scientist employee')], max_length=128, verbose_name='Academic title')),
                ('post', models.CharField(choices=[('assistant', 'Assistant'), ('high_teacher', 'High teacher'), ('docent', 'Docent'), ('professor', 'Professor')], max_length=128, verbose_name='Post')),
                ('total_teaching_experience', models.PositiveSmallIntegerField(verbose_name='Total teaching experience')),
                ('contract_term', models.PositiveSmallIntegerField(verbose_name='Contract term')),
                ('start_term', models.DateField(verbose_name='Start term')),
                ('end_term', models.DateField(verbose_name='End term')),
                ('part_of_stake', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Part of stake')),
                ('professional_development', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='account.professionaldevelopment', verbose_name='Professional development')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pts_users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'PTS',
                'verbose_name_plural': 'PTS employee',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted?')),
                ('street', models.CharField(max_length=256, verbose_name='Street')),
                ('house', models.CharField(max_length=256, verbose_name='House')),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='geo.city', verbose_name='City')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='geo.country', verbose_name='Country')),
                ('region', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='geo.region', verbose_name='Region')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
                'ordering': ['region__name'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='registration_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registered_users', to='account.address', verbose_name='Registration address'),
        ),
        migrations.AddField(
            model_name='user',
            name='resident_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resident_users', to='account.address', verbose_name='Resident address'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]