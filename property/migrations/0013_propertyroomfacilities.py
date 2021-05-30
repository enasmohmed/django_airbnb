# Generated by Django 3.2 on 2021-05-29 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_property_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyRoomFacilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='property_room_fac_images/')),
                ('description', models.TextField(max_length=10000)),
                ('option_service', models.CharField(choices=[('World Class', ' World Class'), ('sweetened', ' sweetened')], max_length=20)),
                ('service_hours_date_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_hours_date_to', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
