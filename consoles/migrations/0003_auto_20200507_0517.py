# Generated by Django 3.0.5 on 2020-05-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0002_auto_20200507_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugsheetmodel',
            name='Defect_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bugsheetmodel',
            name='Developer_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bugsheetmodel',
            name='Reopen_Reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]