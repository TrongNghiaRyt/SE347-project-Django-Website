# Generated by Django 2.2.6 on 2019-12-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_auto_20191225_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcontent',
            name='content',
        ),
        migrations.AddField(
            model_name='blogcontent',
            name='detail',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
