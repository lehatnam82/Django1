# Generated by Django 3.2.7 on 2021-09-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_modelblog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelblog',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]