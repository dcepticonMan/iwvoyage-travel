# Generated by Django 5.1.6 on 2025-04-15 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_section_image_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_hero',
            field=models.ImageField(blank=True, null=True, upload_to='posts/sections/'),
        ),
    ]
