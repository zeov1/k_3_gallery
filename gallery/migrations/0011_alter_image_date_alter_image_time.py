# Generated by Django 5.0.7 on 2024-09-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_alter_image_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
