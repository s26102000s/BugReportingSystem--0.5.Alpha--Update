# Generated by Django 3.0.5 on 2020-05-06 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugsheetmodel',
            name='Developer_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bugsheetmodel',
            name='Project_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bugsheetmodel',
            name='Tester_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
