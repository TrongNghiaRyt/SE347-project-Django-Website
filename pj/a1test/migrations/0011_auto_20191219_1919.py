# Generated by Django 2.2.6 on 2019-12-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1test', '0010_auto_20191219_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
