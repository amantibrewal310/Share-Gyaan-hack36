# Generated by Django 2.2.4 on 2020-02-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_profiles_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='skill',
        ),
        migrations.AlterField(
            model_name='profiles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
