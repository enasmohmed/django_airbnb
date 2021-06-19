# Generated by Django 3.2 on 2021-06-16 15:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0020_alter_propertyreview_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyreview',
            name='rate',
        ),
        migrations.AddField(
            model_name='propertyreview',
            name='rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='propertyreview',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='propertyreview',
            name='feedback',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='propertyreview',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_review', to='property.property'),
        ),
    ]
