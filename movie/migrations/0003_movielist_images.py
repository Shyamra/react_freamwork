# Generated by Django 4.1.7 on 2023-02-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movielist_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='images',
            field=models.ImageField(default='images/None', upload_to='images/'),
        ),
    ]
