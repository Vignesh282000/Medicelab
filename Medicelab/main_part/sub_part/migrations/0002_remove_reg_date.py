# Generated by Django 3.2.3 on 2021-06-24 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='date',
        ),
    ]