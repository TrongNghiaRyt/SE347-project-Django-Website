# Generated by Django 2.2.6 on 2019-12-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1test', '0003_auto_20191211_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]
