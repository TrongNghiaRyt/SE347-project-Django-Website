# Generated by Django 2.2.6 on 2019-12-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1test', '0002_auto_20191211_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
    ]