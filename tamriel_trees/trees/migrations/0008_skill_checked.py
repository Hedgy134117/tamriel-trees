# Generated by Django 2.1 on 2020-03-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0007_auto_20200307_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]