# Generated by Django 2.2.4 on 2020-02-15 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200215_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='phone',
        ),
    ]
