# Generated by Django 3.0.5 on 2020-05-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0004_changelogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='changelogs',
            name='type_of_Change',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
