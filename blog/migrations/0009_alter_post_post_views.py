# Generated by Django 3.2 on 2021-06-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
