# Generated by Django 3.2.3 on 2021-06-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_remove_reg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_ipd',
            name='age',
            field=models.IntegerField(),
        ),
    ]