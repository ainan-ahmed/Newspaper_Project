# Generated by Django 2.2.14 on 2020-07-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200628_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='react',
            field=models.IntegerField(default=0),
        ),
    ]