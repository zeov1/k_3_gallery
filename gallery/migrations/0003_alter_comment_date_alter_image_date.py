# Generated by Django 5.0.7 on 2024-08-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_comment_time_image_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
