# Generated by Django 5.1.6 on 2025-04-27 23:28

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_partner_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='meta_description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, help_text='Optional: Add a custom meta description for SEO.', max_length=1160),
        ),
    ]
