# Generated by Django 2.2.6 on 2019-12-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a1test', '0004_auto_20191218_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='kind',
            field=models.CharField(choices=[('KN', 'Khái niệm'), ('QT', 'Qui tắc'), ('TD', 'Tốc độ'), ('NV', 'Nghiệp vụ'), ('VH', 'Văn hóa'), ('KT', 'Kỹ thuật'), ('CT', 'Cấu tạo'), ('BB', 'Biển báo'), ('SH', 'Sa hình')], max_length=2),
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('exam_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a1test.exam')),
            ],
        ),
    ]
