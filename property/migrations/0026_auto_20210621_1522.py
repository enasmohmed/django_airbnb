# Generated by Django 3.2 on 2021-06-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_auto_20210621_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='name_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
