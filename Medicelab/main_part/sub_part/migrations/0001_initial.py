# Generated by Django 3.2.3 on 2021-06-24 10:30

from django.db import migrations, models
import sub_part.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_ambul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vechile_number', models.CharField(max_length=100)),
                ('vechile_models', models.CharField(max_length=100)),
                ('year_made', models.CharField(max_length=5)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_license', models.CharField(max_length=100)),
                ('driver_contact', models.CharField(max_length=100)),
                ('vechile_type', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_appoint_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('appoint_prio', models.CharField(max_length=5)),
                ('message', models.CharField(max_length=200)),
                ('live_cons', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='admin_bed_lis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bed_type', models.CharField(max_length=100)),
                ('bed_grp', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_bed_stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('bed_type', models.CharField(max_length=100)),
                ('bed_grp', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_birt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('ipd_no', models.CharField(max_length=100)),
                ('report', models.CharField(max_length=100)),
                ('child_photo', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
                ('father_photo', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
                ('mother_photo', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
                ('attach_document', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='admin_blood_bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('store', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('purchase_price', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('donar_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='admin_deat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('ipd_no', models.CharField(max_length=100)),
                ('death_date', models.DateField()),
                ('guardian_name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('receiver_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_ipd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('guard_name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('blood_grp', models.CharField(max_length=5)),
                ('martial_status', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('pat_photo', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='admin_medi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medi_name', models.CharField(max_length=100)),
                ('medi_cate', models.CharField(max_length=100)),
                ('medi_comp', models.CharField(max_length=100)),
                ('medi_composition', models.CharField(max_length=100)),
                ('medi_grp', models.CharField(max_length=100)),
                ('min_level', models.CharField(max_length=100)),
                ('re_order_level', models.CharField(max_length=100)),
                ('vat', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('vat_AC', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('medi_photo', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='admin_mess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_id', models.IntegerField()),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_opd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('guard_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('blood_grp', models.CharField(max_length=5)),
                ('martial_status', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('pat_photo', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='admin_opeartionthea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_id', models.IntegerField()),
                ('opeartion_date', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('operation_name', models.CharField(max_length=50)),
                ('operation_type', models.CharField(max_length=50)),
                ('consultant', models.CharField(max_length=50)),
                ('applied_charge', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('attach_document', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='admin_patho_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=100)),
                ('test_type', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=100)),
                ('report_daya', models.CharField(max_length=100)),
                ('charge_cate', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('std_charge', models.CharField(max_length=100)),
                ('test_para_name', models.CharField(max_length=100)),
                ('ref_range', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_phar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('pat_name', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_profile_edi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('martial_status', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('guard_name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='admin_radio_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=100)),
                ('test_type', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=100)),
                ('report_daya', models.CharField(max_length=100)),
                ('charge_cate', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('std_charge', models.CharField(max_length=100)),
                ('test_para_name', models.CharField(max_length=100)),
                ('ref_range', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='admin_staffD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
                ('staff_first_name', models.CharField(max_length=100)),
                ('staff_last_name', models.CharField(max_length=100)),
                ('staff_father_name', models.CharField(max_length=100)),
                ('staff_mother_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('martial_status', models.CharField(max_length=100)),
                ('blood_grp', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('date_of_joining', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('staff_photo', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
                ('current_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='admin_visitor_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('purpose', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('id_card', models.CharField(max_length=20)),
                ('no_of_per', models.IntegerField()),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('message', models.CharField(max_length=100)),
                ('attach_document', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='landing_feedback_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='landing_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.CharField(max_length=100)),
                ('reject', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='need_bloo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(max_length=100)),
                ('blood_priority', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='order_medic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('blood_grp', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('medi_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_appoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('appoint_prio', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
                ('live_cons', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_com_pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('martial_status', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('guard_name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='user_liveco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_id', models.CharField(max_length=100)),
                ('pat_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('live_cons', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_profile_edi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('martial_status', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('guard_name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=sub_part.models.filepath)),
            ],
        ),
    ]
