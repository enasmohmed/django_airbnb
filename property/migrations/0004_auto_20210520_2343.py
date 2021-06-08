# Generated by Django 3.2 on 2021-05-20 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_property_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ImageField(upload_to='property_image/'),
        ),
        migrations.AlterField(
            model_name='propertyimages',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_image', to='property.property'),
        ),
    ]
