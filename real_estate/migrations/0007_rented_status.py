# Generated by Django 3.2.9 on 2022-03-28 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0006_rented_user_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rented',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
