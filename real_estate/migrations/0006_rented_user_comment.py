# Generated by Django 3.2.9 on 2022-03-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0005_auto_20220328_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='rented',
            name='user_comment',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]