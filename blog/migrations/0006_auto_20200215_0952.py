# Generated by Django 3.0.3 on 2020-02-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200215_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/test.jpg', upload_to='images/'),
        ),
    ]
