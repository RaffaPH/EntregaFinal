# Generated by Django 4.0.4 on 2022-06-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
