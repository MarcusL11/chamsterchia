# Generated by Django 5.0 on 2023-12-25 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_markdowncontent_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='markdowncontent',
            options={'verbose_name_plural': 'Blog content'},
        ),
    ]
