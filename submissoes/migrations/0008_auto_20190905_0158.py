# Generated by Django 2.2.3 on 2019-09-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissoes', '0007_auto_20190829_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='submissoes'),
        ),
    ]
