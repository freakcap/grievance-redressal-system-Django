# Generated by Django 3.0.4 on 2020-04-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200423_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='student',
            name='stu_roll_no',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
