# Generated by Django 5.0 on 2023-12-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chamster',
            fields=[
                ('id', models.CharField(default=0, max_length=100, primary_key=True, serialize=False)),
                ('encoded_id', models.CharField(default=0, max_length=100)),
                ('owner_address', models.CharField(default=0, max_length=100)),
                ('data_uri', models.URLField(default=0, max_length=250)),
                ('thumbnail_uri', models.URLField(default=0, max_length=250)),
                ('preview_uri', models.URLField(default=0, max_length=250)),
                ('name', models.CharField(default=0, max_length=100)),
                ('background', models.CharField(default=0, max_length=50)),
                ('fur', models.CharField(default=0, max_length=50)),
                ('shirt', models.CharField(default=0, max_length=50)),
                ('pants', models.CharField(default=0, max_length=50)),
                ('head', models.CharField(default=0, max_length=50)),
                ('eyes', models.CharField(default=0, max_length=50)),
                ('club', models.CharField(default=0, max_length=50)),
                ('power', models.IntegerField(default=0)),
                ('putting', models.IntegerField(default=0)),
                ('accuracy', models.IntegerField(default=0)),
                ('recovery', models.IntegerField(default=0)),
                ('luck', models.IntegerField(default=0)),
                ('specialty', models.CharField(default=0, max_length=50)),
                ('tsi', models.IntegerField(default=0)),
            ],
        ),
    ]
