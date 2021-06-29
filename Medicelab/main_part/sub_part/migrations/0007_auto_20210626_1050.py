# Generated by Django 3.2.3 on 2021-06-26 05:20

from django.db import migrations, models
import sub_part.models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_auto_20210626_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_radio_test',
            name='report',
            field=models.FileField(blank=True, null=True, upload_to=sub_part.models.filepath),
        ),
        migrations.AlterField(
            model_name='admin_radio_test',
            name='short_name',
            field=models.IntegerField(),
        ),
    ]
