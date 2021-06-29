from django.db import models

# Create your models here.
from django.db import models
import os,datetime

# Create your models here.

def filepath(request,filename):
    old_filename=filename
    timenow=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename= "%s%s" % (timenow,old_filename)
    return os.path.join('uploads/',filename)


class reg(models.Model):
    first_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    department=models.EmailField()

    def __str__(self):
        return self.first_name

class admin_reg(models.Model):
    first_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class admin_appoint_model(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField()
    gender=models.CharField(max_length=20)
    doctor=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    appoint_prio=models.CharField(max_length=5)
    message=models.CharField(max_length=200)
    live_cons=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class admin_visitor_model(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField()
    purpose=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    id_card=models.CharField(max_length=20)
    no_of_per=models.IntegerField()
    in_time=models.TimeField()
    out_time=models.TimeField()
    message=models.CharField(max_length=100)
    attach_document=models.ImageField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.name

class admin_opd(models.Model):
    name=models.CharField(max_length=20)
    guard_name=models.CharField(max_length=20)
    age=models.IntegerField()
    date=models.DateField()
    gender=models.CharField(max_length=20)
    blood_grp=models.CharField(max_length=5)
    martial_status=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    pat_photo=models.ImageField(upload_to=filepath,null=True,blank=True)
    report=models.FileField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.name

class admin_ipd(models.Model):
    name=models.CharField(max_length=20)
    guard_name=models.CharField(max_length=20)
    age=models.IntegerField()
    date=models.DateField()
    gender=models.CharField(max_length=20)
    blood_grp=models.CharField(max_length=5)
    martial_status=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    pat_photo=models.ImageField(upload_to=filepath,null=True,blank=True)
    report=models.FileField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.name

class admin_medi(models.Model):
    medi_name=models.CharField(max_length=100)
    medi_cate=models.CharField(max_length=100)
    medi_comp=models.CharField(max_length=100)
    medi_composition=models.CharField(max_length=100)
    medi_grp=models.CharField(max_length=100)
    unit=models.CharField(max_length=100)
    min_level=models.CharField(max_length=100)
    re_order_level=models.CharField(max_length=100)
    vat=models.CharField(max_length=100)
    unit=models.CharField(max_length=100)
    vat_AC=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    medi_photo=models.ImageField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.medi_name

class admin_phar(models.Model):
    bill_no=models.CharField(max_length=100)
    date=models.DateField()
    pat_name=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    total=models.CharField(max_length=100)
    
    def __str__(self):
        return self.bill_no

class admin_patho_test(models.Model):
    test_name=models.CharField(max_length=100)
    short_name=models.IntegerField()
    test_type=models.CharField(max_length=100)
    category_name=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    method=models.CharField(max_length=100)
    report_daya=models.CharField(max_length=100)
    charge_cate=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    std_charge=models.CharField(max_length=100)
    test_para_name=models.CharField(max_length=100)
    ref_range=models.CharField(max_length=100)
    unit=models.CharField(max_length=100)
    report=models.FileField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.test_name

class admin_radio_test(models.Model):
    test_name=models.CharField(max_length=100)
    short_name=models.IntegerField()
    test_type=models.CharField(max_length=100)
    category_name=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    method=models.CharField(max_length=100)
    report_daya=models.CharField(max_length=100)
    charge_cate=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    std_charge=models.CharField(max_length=100)
    test_para_name=models.CharField(max_length=100)
    ref_range=models.CharField(max_length=100)
    unit=models.CharField(max_length=100)
    report=models.FileField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.test_name

class admin_opeartionthea(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_id=models.IntegerField()
    opeartion_date=models.DateField()
    gender=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    operation_name=models.CharField(max_length=50)
    operation_type=models.CharField(max_length=50)
    consultant=models.CharField(max_length=50)
    applied_charge=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
    attach_document=models.ImageField(upload_to=filepath,null=True,blank=True)


    def __str__(self):
        return self.patient_name

class admin_blood_bank(models.Model):
    blood_type=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    store=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    purchase_price=models.CharField(max_length=100)
    date=models.DateField()
    description=models.CharField(max_length=100)
    donar_name=models.CharField(max_length=50)

    def __str__(self):
        return self.donar_name

class admin_ambul(models.Model):
    vechile_number=models.CharField(max_length=100)
    vechile_models=models.CharField(max_length=100)
    year_made=models.CharField(max_length=5)
    driver_name=models.CharField(max_length=100)
    driver_license=models.CharField(max_length=100)
    driver_contact=models.CharField(max_length=100)
    vechile_type=models.CharField(max_length=100)
    note=models.CharField(max_length=100)

    def __str__(self):
        return self.vechile_number

class admin_birt(models.Model):
    child_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    birth_date=models.DateField()
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    ipd_no=models.CharField(max_length=100)
    report=models.CharField(max_length=100)
    child_photo=models.ImageField(upload_to=filepath,null=True,blank=True)
    father_photo=models.ImageField(upload_to=filepath,null=True,blank=True)
    mother_photo=models.ImageField(upload_to=filepath,null=True,blank=True)
    attach_document=models.ImageField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.child_name

class admin_deat(models.Model):
    patient_name=models.CharField(max_length=100)
    ipd_no=models.CharField(max_length=100)
    death_date=models.DateField()
    guardian_name=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    receiver_name=models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name

class landing_form(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    date=models.DateField()
    department=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class user_appoin(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField()
    gender=models.CharField(max_length=20)
    doctor=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    appoint_prio=models.CharField(max_length=100)
    message=models.CharField(max_length=200)
    live_cons=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class landing_feedback_form(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class admin_staffD(models.Model):
    staff_id=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    specialist=models.CharField(max_length=100)
    staff_first_name=models.CharField(max_length=100)
    staff_last_name=models.CharField(max_length=100)
    staff_father_name=models.CharField(max_length=100)
    staff_mother_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    martial_status=models.CharField(max_length=100)
    blood_grp=models.CharField(max_length=100)
    date=models.DateField()
    date_of_joining=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    email=models.EmailField()
    staff_photo=models.ImageField(upload_to=filepath,null=True,blank=True)
    current_address=models.CharField(max_length=100)
    permanent_address=models.CharField(max_length=100)

    def __str__(self):
        return self.staff_id

class admin_bed_lis(models.Model):
    name=models.CharField(max_length=100)
    bed_type=models.CharField(max_length=100)
    bed_grp=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class admin_bed_stat(models.Model):
    number=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    bed_type=models.CharField(max_length=100)
    bed_grp=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.number

class admin_profile_edi(models.Model):
    patient_id=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    martial_status=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    guard_name=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.patient_id
    
class user_liveco(models.Model):
    pat_id=models.CharField(max_length=100)
    pat_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    live_cons=models.CharField(max_length=100)

    def __str__(self):
        return self.pat_id

class messages(models.Model):
    accept=models.CharField(max_length=100)
    reject=models.CharField(max_length=100)
    
class need_bloo(models.Model):
    blood_type=models.CharField(max_length=100)
    blood_priority=models.CharField(max_length=100)

    def __str__(self):
        return self.blood_type

class user_profile_edi(models.Model):
    patient_id=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    martial_status=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    guard_name=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.patient_id
    
class order_medic(models.Model):
    pat_id=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    blood_grp=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    medi_name=models.CharField(max_length=100)
    quantity=models.IntegerField()

    def __str__(self):
        return self.pat_id

class admin_mess(models.Model):
    pat_id=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.message

class user_com_pro(models.Model):
    gender=models.CharField(max_length=100)
    martial_status=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    guard_name=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.email
