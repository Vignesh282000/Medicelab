# Generated by Django 3.2.3 on 2021-06-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_alter_reg_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_mess',
            name='pat_id',
            field=models.CharField(max_length=100),
        ),
    ]