# Generated by Django 4.1.3 on 2023-01-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convertor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion',
            name='file',
            field=models.FileField(upload_to='mp3/'),
        ),
    ]
