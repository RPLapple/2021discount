# Generated by Django 3.1.7 on 2021-04-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0005_supermarket_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]