# Generated by Django 3.2.7 on 2021-09-12 08:54

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelblog',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]
