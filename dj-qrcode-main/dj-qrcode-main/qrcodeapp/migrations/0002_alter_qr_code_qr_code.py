# Generated by Django 4.2.1 on 2023-05-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_code',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_code'),
        ),
    ]