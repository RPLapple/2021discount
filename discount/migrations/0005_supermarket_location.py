# Generated by Django 3.1.7 on 2021-04-09 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0004_auto_20210409_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='supermarket',
            name='location',
            field=models.CharField(default='Berlin', max_length=40),
        ),
    ]
