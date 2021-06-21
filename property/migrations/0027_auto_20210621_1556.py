# Generated by Django 3.2 on 2021-06-21 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_auto_20210621_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='description_ar',
        ),
        migrations.RemoveField(
            model_name='property',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='property',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='property',
            name='name_en',
        ),
        migrations.AddField(
            model_name='propertyreview',
            name='feedback_ar',
            field=models.TextField(default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='propertyreview',
            name='feedback_en',
            field=models.TextField(default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='propertyreview',
            name='property_ar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_review', to='property.property'),
        ),
        migrations.AddField(
            model_name='propertyreview',
            name='property_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_review', to='property.property'),
        ),
    ]
