# Generated by Django 3.2 on 2021-06-09 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_views',
        ),
    ]
