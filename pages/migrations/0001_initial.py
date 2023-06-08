# Generated by Django 4.1.7 on 2023-03-16 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.IntegerField()),
                ('cin', models.IntegerField(error_messages={'unique': 'Le numéro de cin est déja utilisé'}, unique=True)),
                ('etablissement', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('date_naissance', models.DateField()),
                ('telephone', models.IntegerField(error_messages={'unique': 'Le numéro est déja utilisé'}, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('etablissement', models.CharField(max_length=100)),
                ('classe', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DemandeStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_stage', models.CharField(max_length=20)),
                ('etat', models.IntegerField(default=0)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='DemandeAcces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MotPasse', models.CharField(max_length=16, null=True)),
                ('NomUtilisateur', models.CharField(max_length=100, null=True)),
                ('etat', models.IntegerField(default=0)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Bureautique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('niveau', models.CharField(max_length=100)),
                ('etat', models.IntegerField(default=0)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Applicative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('etat', models.IntegerField(default=0)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.employee')),
            ],
        ),
    ]
