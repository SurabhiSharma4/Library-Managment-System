# Generated by Django 4.2.7 on 2025-04-17 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
    ]
