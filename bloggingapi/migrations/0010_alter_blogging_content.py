# Generated by Django 5.0.6 on 2024-11-23 10:54

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloggingapi', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogging',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
