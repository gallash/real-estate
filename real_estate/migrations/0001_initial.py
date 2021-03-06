# Generated by Django 3.2.9 on 2022-03-24 03:38

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
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('SP', 'São Paulo'), ('RS', 'Rio Grande do Sul')], max_length=2)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('type_of_place', models.CharField(choices=[('Apto', 'Apartamento'), ('Casa', 'Casa'), ('Kit', 'Kitnet')], max_length=10)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rented',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='real_estate.place')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
