# Generated by Django 2.0.1 on 2018-01-14 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20180114_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='faculty',
        ),
        migrations.AddField(
            model_name='groups',
            name='stud',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.students', verbose_name='Студент'),
            preserve_default=False,
        ),
    ]
