# Generated by Django 3.2.3 on 2021-06-25 08:34

from django.db import migrations, models
import sub_part.models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0003_alter_admin_ipd_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_opd',
            name='report',
            field=models.FileField(blank=True, null=True, upload_to=sub_part.models.filepath),
        ),
    ]
