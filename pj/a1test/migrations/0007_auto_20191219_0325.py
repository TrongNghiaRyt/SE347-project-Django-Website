# Generated by Django 2.2.6 on 2019-12-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1test', '0006_questiontype_kinds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='time',
            field=models.IntegerField(default=20),
        ),
    ]
