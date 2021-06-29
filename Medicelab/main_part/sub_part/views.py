from typing import ChainMap
from django.shortcuts import render
import os
# Create your views here.
from django.conf import settings
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import redirect, render
from . models import admin_ambul, admin_bed_stat,admin_mess, admin_phar, admin_profile_edi,admin_staffD, landing_feedback_form, landing_form, messages, need_bloo, order_medic,user_appoin,reg,admin_reg,admin_appoint_model,admin_visitor_model,admin_opd,admin_ipd,admin_medi,admin_patho_test,admin_radio_test,admin_opeartionthea,admin_blood_bank,admin_birt,admin_deat,admin_bed_lis, user_com_pro, user_liveco, user_profile_edi
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log
import easygui
from django.core.mail import send_mail

multi_user_name=''
admin_multi_user_name=''
user_current_password=''
user_current_id=''
admin_current_password=''
admin_current_id=''

# Create your views here.
def download(request,path):
    file_path=os.path.join(settings.MEDIAROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404

def index(request):
    disp11=admin_staffD.objects.all()
    return render(request,'index.html',{'disp11':disp11})

def Userlogin(request):
    return render(request,'Loginpage.html')

def register(request):
    return render(request,'registerpage.html')

def adminlogin(request):
    return render(request,'Admin.html')

def admin_register(request):
    return render(request,'Admin-reg.html')

def admin_dash(request):
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'dashboard-analytics.html',{'data':data})

def admin_appointdetails(request):
    disp=admin_appoint_model.objects.all()
    disp11=admin_staffD.objects.all()
    disp12=user_appoin.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    disp10=landing_form.objects.all()
    return render(request,'AppointDetails.html',{'disp':disp,'disp11':disp11,'disp12':disp12,'data':data,'disp10':disp10})

def admin_visitor(request):
    disp1=admin_visitor_model.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'VisitorPage.html',{'disp1':disp1,'data':data})

def admin_OPD(request):
    disp2=admin_opd.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'OPD.html',{'disp2':disp2,'data':data})

def admin_IPD(request):
    disp3=admin_ipd.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'IPD.html',{'disp3':disp3,'data':data})

def admin_pharmacy(request):
    disp4=admin_phar.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Pharmacy.html',{'disp4':disp4,'data':data})

def admin_pharmacy_medicine(request):
    disp4=admin_medi.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Pharmacy-Medicine.html',{'disp4':disp4,'data':data})

def admin_pathology(request):
    disp5=admin_patho_test.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Pathology.html',{'disp5':disp5,'data':data})

def admin_pathology_test(request):
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Pathology-Test.html',{'data':data})

def admin_radiology(request):
    disp6=admin_radio_test.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Radiology.html',{'disp6':disp6,'data':data})

def admin_radiology_test(request):
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Radiology-Test.html',{'data':data})    

def admin_OT(request):
    disp7=admin_opeartionthea.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'OperationTheatre.html',{'disp7':disp7,'data':data})

def admin_blood(request):
    disp8=admin_blood_bank.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'BloodBank.html',{'disp8':disp8,'data':data})

def admin_livecons(request):
    disp17=user_liveco.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'LiveCons.html',{'disp17':disp17,'data':data})

def admin_ambulance(request):
    disp9=admin_ambul.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Ambulance.html',{'disp9':disp9,'data':data})

def admin_birth(request):
    disp10=admin_birt.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Birth.html',{'disp10':disp10,'data':data})
    
def admin_death(request):
    disp11=admin_deat.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Death.html',{'disp11':disp11,'data':data})

def admin_staffdetails(request):
    disp10=admin_staffD.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'StaffDetails.html',{'disp10':disp10,'data':data})

def admin_bedstatus(request):
    disp12=admin_bed_stat.objects.all()
    disp11=admin_bed_lis.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'BedStatus.html',{'disp12':disp12,'disp11':disp11,'data':data})

def admin_bedlist(request):
    disp11=admin_bed_lis.objects.all()
    disp12=admin_bed_stat.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'BedList.html',{'disp11':disp11,'disp12':disp12,'data':data})

def admin_message(request):
    disp25=user_com_pro.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    disp30=reg.objects.all()
    return render(request,'Messaging.html',{'disp25':disp25,'data':data,'disp30':disp30})

def admin_profile(request):
    disp13=admin_profile_edi.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    a_curr_id=admin_reg.objects.get(id=admin_current_id)
    return render(request,'Admin-profile.html',{'disp13':disp13,'data':data,'a_curr_id':a_curr_id})

def admin_changepass(request):
    var20=admin_reg.objects.all()
    return render(request,'Changepassword.html',{'var20':var20})

def admin_profile_edit(request,id):
    var21=admin_profile_edi.objects.get(id=id)
    return render(request,'admin_profile_edit.html',{'var21':var21})

def admin_ordered_medicine(request):
    disp4=admin_medi.objects.all()
    disp5=order_medic.objects.all()
    data=admin_reg.objects.get(username=admin_multi_user_name)
    return render(request,'Ordered_Medicine.html',{'disp4':disp4,'disp5':disp5,'data':data})

def admin_profile_update(request,id):
    var22=admin_profile_edi(id=id)
    var22.patient_id=request.POST.get('patient_id')
    var22.gender=request.POST.get('gender')
    var22.martial_status=request.POST.get('martial_status')
    var22.phone=request.POST.get('phone')
    var22.email=request.POST.get('email')
    var22.address=request.POST.get('address')
    var22.age=request.POST.get('age')
    var22.guard_name=request.POST.get('guard_name')
    if len(request.FILES) != 0:
        var22.profile_pic=request.FILES['profile_pic']
    var22.save()
    easygui.msgbox("Profile has been Updated!...")
    return redirect(admin_profile)

def user_profile_edit(request,id):
    var25=user_profile_edi.objects.get(id=id)
    return render(request,'user_profile_edit.html',{'var25':var25})

def user_profile_update(request,id):
    if request.method=='POST':
        var22=user_profile_edi(id=id)
        var22.patient_id=request.POST.get('patient_id')
        var22.gender=request.POST.get('gender')
        var22.martial_status=request.POST.get('martial_status')
        var22.phone=request.POST.get('phone')
        var22.email=request.POST.get('email')
        var22.address=request.POST.get('address')
        var22.age=request.POST.get('age')
        var22.guard_name=request.POST.get('guard_name')
        if len(request.FILES) != 0:
            var22.profile_pic=request.FILES['profile_pic']
        var22.save()
        easygui.msgbox("Profile has been Updated!...")
        return redirect(user_profile)

def user_appoint(request):
    disp10=user_appoin.objects.all()
    view_doc=admin_staffD.objects.all()
    disp13=admin_profile_edi.objects.all()
    disp30=admin_mess.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    return render(request,'User-AppointDetails.html',{'disp10':disp10,'view_doc':view_doc,'disp13':disp13,'disp30':disp30,'ut_data':ut_data})

def user_opd(request):
    disp=admin_opd.objects.all()
    disp1=user_com_pro.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    curr_id=reg.objects.get(id=user_current_id)
    return render(request,'User-OPD.html',{'disp':disp,'disp1':disp1,'ut_data':ut_data,'curr_id':curr_id})

def user_ipd(request):
    disp=admin_ipd.objects.all()
    disp1=user_com_pro.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    curr_id=reg.objects.get(id=user_current_id)
    return render(request,'User-IPD.html',{'disp':disp,'disp1':disp1,'ut_data':ut_data,'curr_id':curr_id})

def user_pharmacy(request):
    disp4=admin_medi.objects.all()
    disp5=order_medic.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    return render(request,'User-Pharmacy.html',{'disp4':disp4,'disp5':disp5,'ut_data':ut_data})

def user_pathology(request):
    disp5=admin_patho_test.objects.all()
    disp1=user_com_pro.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    curr_id=reg.objects.get(id=user_current_id)
    return render(request,'User-Pathology.html',{'disp5':disp5,'disp1':disp1,'ut_data':ut_data,'curr_id':curr_id})

def user_radiology(request):
    disp5=admin_radio_test.objects.all()
    disp1=user_com_pro.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    curr_id=reg.objects.get(id=user_current_id)
    return render(request,'User-Radiology.html',{'disp5':disp5,'disp1':disp1,'ut_data':ut_data,'curr_id':curr_id})

def user_operationtheatre(request):
    disp7=admin_opeartionthea.objects.all()
    disp25=user_com_pro.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    curr_id=reg.objects.get(id=user_current_id)
    return render(request,'User-OperaTheatre.html',{'disp7':disp7,'disp25':disp25,'ut_data':ut_data,'curr_id':curr_id})

def user_ambulance(request):
    ut_data=reg.objects.get(username=multi_user_name)
    return render(request,'User-Ambulance.html',{'ut_data':ut_data})

def user_blood(request):
    disp17=need_bloo.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    return render(request,'User-BloodBank.html',{'disp17':disp17,'ut_data':ut_data})

def user_livecons(request):
    ut_data=reg.objects.get(username=multi_user_name)
    return render(request,'User-Livecon.html',{'ut_data':ut_data})

def user_profile(request):
    disp_data=user_com_pro.objects.all()
    var30=reg.objects.all()
    ut_data=reg.objects.get(username=multi_user_name)
    curr_id=reg.objects.get(id=user_current_id)
    return render(request,'User-Profile.html',{'disp_data':disp_data,'var30':var30,'ut_data':ut_data,'curr_id':curr_id})

def user_complete_profile(request):
    return render(request,'user_complete_profile.html')

def user_view_message(request,id):
    disp31=admin_mess.objects.get(id=id)
    disp13=admin_profile_edi.objects.all()
    return render(request,'user_view_message.html',{'disp31':disp31,'disp13':disp13})

def admin_app_edit(request,id):
    edit1=admin_appoint_model.objects.get(id=id)
    return render(request,'admin_appoint_edit.html',{'edit1':edit1})

def admin_app_update(request,id):
    update1=admin_appoint_model(id=id,name=request.POST['name'],
                                 date=request.POST['date'],
                                 gender=request.POST['gender'],
                                 doctor=request.POST['doctor'],
                                 phone=request.POST['phone'],
                                 email=request.POST['email'],
                                 appoint_prio=request.POST['app_prio'],
                                 message=request.POST['message'],
                                 live_cons=request.POST['live_cons'])
    update1.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_appointdetails)

def admin_app_delete(request,id):
    delete1=admin_appoint_model.objects.get(id=id)
    delete1.delete()
    return redirect(admin_appointdetails)

def admin_vis_edit(request,id):
    edit2=admin_visitor_model.objects.get(id=id)
    return render(request,'admin_visitor_edit.html',{'edit2':edit2})

def admin_vis_update(request,id):
    update2=admin_visitor_model(id=id,name=request.POST['name'],
                                 date=request.POST['date'],
                                 purpose=request.POST['purpose'],
                                 phone=request.POST['phone'],
                                 id_card=request.POST['id_card'],
                                 no_of_per=request.POST['no_of_per'],
                                 in_time=request.POST['in_time'],
                                 out_time=request.POST['out_time'],
                                 message=request.POST['message'])
    update2.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_visitor)

def admin_vis_delete(request,id):
    delete2=admin_visitor_model.objects.get(id=id)
    delete2.delete()
    return redirect(admin_visitor)

def admin_opd_edit(request,id):
    edit3=admin_opd.objects.get(id=id)
    return render(request,'admin_op_edit.html',{'edit3':edit3})

def admin_opd_update(request,id):
    update3=admin_opd(id=id,name=request.POST['name'],
                       guard_name=request.POST['guard_name'],
                       age=request.POST['age'],
                       date=request.POST['date'],
                       gender=request.POST['gender'],
                       blood_grp=request.POST['blood_grp'],
                       martial_status=request.POST['martial_status'],
                       phone=request.POST['phone'],
                       email=request.POST['email'],
                       address=request.POST['address'],
                       remarks=request.POST['remarks'],
                       message=request.POST['message'])
    update3.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_OPD)

def admin_opd_delete(request,id):
    delete3=admin_opd.objects.get(id=id)
    delete3.delete()
    return redirect(admin_OPD)

def user_changepass_edit(request,id):
    chan_pass=reg.objects.get(id=id)
    curr_pass=reg.objects.get(password=user_current_password)
    return render(request,'Changepassword.html',{'chan_pass':chan_pass,'curr_pass':curr_pass})

def user_changepass_update(request,id):
    curr_pass=reg.objects.get(password=user_current_password)
    if request.method == 'POST':
        current_password=request.POST['current_password']
        if current_password == curr_pass.password :
            update_pass=reg(id=id,first_name=request.POST['first_name'],
                 username=request.POST['username'],
                 last_name=request.POST['lastname'],
                 password=request.POST['new_password'],
                 department=request.POST['department'])
            update_pass.save()
            easygui.msgbox("Your Password has been Successfully Changed!....")
            return redirect(user_profile)
        else :
            easygui.msgbox("Your Current Password Mismatches!.....")
            return redirect(user_profile)
    return redirect(user_profile)

def admin_changepass_edit(request,id):
    a_chan_pass=admin_reg.objects.get(id=id)
    a_curr_pass=admin_reg.objects.get(password=admin_current_password)
    return render(request,'admin_changepass.html',{'a_chan_pass':a_chan_pass,'a_curr_pass':a_curr_pass})

def admin_changepass_update(request,id):
    a_curr_pass=admin_reg.objects.get(password=admin_current_password)
    if request.method == 'POST':
        current_password=request.POST['current_password']
        if current_password == a_curr_pass.password :
            update_pass=admin_reg(id=id,first_name=request.POST['first_name'],
                 username=request.POST['username'],
                 last_name=request.POST['lastname'],
                 password=request.POST['new_password'])
            update_pass.save()
            easygui.msgbox("Your Password has been Successfully Changed!....")
            return redirect(admin_profile)
        else :
            easygui.msgbox("Your Current Password Mismatches!.....")
            return redirect(admin_profile)
    return redirect(admin_profile)
    

            
def admin_ipd_edit(request,id):
    edit4=admin_ipd.objects.get(id=id)
    return render(request,'admin_ip_edit.html',{'edit4':edit4})

def admin_ipd_update(request,id):
    update4=admin_ipd(id=id,name=request.POST['name'],
                       guard_name=request.POST['guard_name'],
                       age=request.POST['age'],
                       date=request.POST['date'],
                       gender=request.POST['gender'],
                       blood_grp=request.POST['blood_grp'],
                       martial_status=request.POST['martial_status'],
                       phone=request.POST['phone'],
                       email=request.POST['email'],
                       address=request.POST['address'],
                       remarks=request.POST['remarks'],
                       message=request.POST['message'])
    update4.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_IPD)

def admin_ipd_delete(request,id):
    delete4=admin_ipd.objects.get(id=id)
    delete4.delete()
    return redirect(admin_IPD)

def admin_phar_edit(request,id):
    edit5=admin_medi.objects.get(id=id)
    return render(request,'admin_phar_edit.html',{'edit5':edit5})

def admin_phar_update(request,id):
    update5=admin_medi(id=id,medi_name=request.POST['medi_name'],
                            medi_cate=request.POST['medi_cate'],
                            medi_comp=request.POST['medi_comp'],
                            medi_composition=request.POST['medi_composition'],
                            medi_grp=request.POST['medi_grp'],
                            min_level=request.POST['min_level'],
                            re_order_level=request.POST['re_order_level'],
                            unit=request.POST['unit'],
                            vat=request.POST['vat'],
                            vat_AC=request.POST['vat_AC'],
                            message=request.POST['message'])
    update5.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_pharmacy_medicine)

def admin_phar_delete(request,id):
    delete5=admin_medi.objects.get(id=id)
    delete5.delete()
    return redirect(admin_pharmacy_medicine)

def admin_patho_edit(request,id):
    edit6=admin_patho_test.objects.get(id=id)
    return render(request,'admin_patho_edit.html',{'edit6':edit6})

def admin_patho_update(request,id):
    update6=admin_patho_test(id=id,test_name=request.POST['test_name'],
                              short_name=request.POST['short_name'],
                              test_type=request.POST['test_type'],
                              category_name=request.POST['category_name'],
                              sub_category=request.POST['sub_category'],
                              method=request.POST['method'],
                              report_daya=request.POST['report_days'],
                              charge_cate=request.POST['charge_cate'],
                              code=request.POST['code'],
                              std_charge=request.POST['std_charge'],
                              test_para_name=request.POST['test_para_name'],
                              ref_range=request.POST['ref_range'],
                              unit=request.POST['unit'])
    update6.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_pathology)

def admin_patho_delete(request,id):
    delete6=admin_patho_test.objects.get(id=id)
    delete6.delete()
    return redirect(admin_pathology)

def admin_radio_edit(request,id):
    edit7=admin_radio_test.objects.get(id=id)
    return render(request,'admin_radio_edit.html',{'edit7':edit7})

def admin_radio_update(request,id):
    update7=admin_radio_test(id=id,test_name=request.POST['test_name'],
                              short_name=request.POST['short_name'],
                              test_type=request.POST['test_type'],
                              category_name=request.POST['category_name'],
                              sub_category=request.POST['sub_category'],
                              method=request.POST['method'],
                              report_daya=request.POST['report_days'],
                              charge_cate=request.POST['charge_cate'],
                              code=request.POST['code'],
                              std_charge=request.POST['std_charge'],
                              test_para_name=request.POST['test_para_name'],
                              ref_range=request.POST['ref_range'],
                              unit=request.POST['unit'])
    update7.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_radiology)

def admin_radio_delete(request,id):
    delete7=admin_radio_test.objects.get(id=id)
    delete7.delete()
    return redirect(admin_radiology)

def admin_operation_edit(request,id):
    edit8=admin_opeartionthea.objects.get(id=id)
    return render(request,'admin_operation_edit.html',{'edit8':edit8})

def admin_operation_update(request,id):
    update8=admin_opeartionthea(id=id,patient_name=request.POST['patient_name'],
                                 patient_id=request.POST['patient_id'],
                                 opeartion_date=request.POST['operation_date'],
                                 gender=request.POST['gender'],
                                 phone=request.POST['phone'],
                                 operation_name=request.POST['operation_name'],
                                 operation_type=request.POST['operation_type'],
                                 consultant=request.POST['consultant'],
                                 applied_charge=request.POST['applied_charge'],
                                 message=request.POST['message'])
    update8.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(admin_OT)

def admin_operation_delete(request,id):
    delete8=admin_opeartionthea.objects.get(id=id)
    delete8.delete()
    return redirect(admin_OT)

def admin_blood_edit(request,id):
    edit9=admin_blood_bank.objects.get(id=id)
    return render(request,'admin_blood_edit.html',{'edit9':edit9})

def admin_blood_update(request,id):
    update9=admin_blood_bank(id=id,blood_type=request.POST['blood_type'],
                               item=request.POST['item'],
                               supplier=request.POST['supplier'],
                               store=request.POST['store'],
                               quantity=request.POST['quantity'],
                               purchase_price=request.POST['purchase_price'],
                               date=request.POST['date'],
                               description=request.POST['description'],
                               donar_name=request.POST['donar_name'])
    update9.save()
    easygui.msgbox('Data has been successfully Updated!...',title='UPDATE')
    return redirect(admin_blood)

def admin_blood_delete(request,id):
    delete9=admin_blood_bank.objects.get(id=id)
    delete9.delete()
    return redirect(admin_blood)

def admin_ambulance_edit(request,id):
    edit10=admin_ambul.objects.get(id=id)
    return render(request,'admin_ambulance_edit.html',{'edit10':edit10})

def admin_ambulance_update(request,id):
    update10=admin_ambul(id=id,vechile_number=request.POST['vechile_number'],
                          vechile_models=request.POST['vechile_model'],
                          year_made=request.POST['year_made'],
                          driver_name=request.POST['driver_name'],
                          driver_license=request.POST['driver_license'],
                          driver_contact=request.POST['driver_contact'],
                          vechile_type=request.POST['vechile_type'],
                          note=request.POST['note'])
    update10.save()
    easygui.msgbox("Data has been successfully Updated!....")
    return redirect(admin_ambulance)

def admin_ambulance_delete(request,id):
    delete10=admin_ambul.objects.get(id=id)
    delete10.delete()
    return redirect(admin_ambulance)

def admin_birth_edit(request,id):
    edit11=admin_birt.objects.get(id=id)
    return render(request,'admin_birth_edit.html',{'edit11':edit11})

def admin_birth_update(request,id):
    update11=admin_birt(id=id)
    update11.child_name=request.POST.get('child_name')
    update11.gender=request.POST.get('gender')
    update11.weight=request.POST.get('weight')
    update11.birth_date=request.POST.get('birth_date')
    update11.phone=request.POST.get('phone')
    update11.address=request.POST.get('address')
    update11.father_name=request.POST.get('father_name')
    update11.mother_name=request.POST.get('mother_name')
    update11.ipd_no=request.POST.get('ipd_no')
    update11.report=request.POST.get('report')
    update11.save()
    easygui.msgbox('Data has been updated successfully!...')
    return redirect(admin_birth)

def admin_birth_delete(request,id):
    delete11=admin_birt.objects.get(id=id)
    delete11.delete()
    return redirect(admin_birth)

def admin_death_edit(request,id):
    edit12=admin_deat.objects.get(id=id)
    return render(request,'admin_death_edit.html',{'edit12':edit12})

def admin_death_update(request,id):
    update12=admin_deat(id=id,patient_name=request.POST['patient_name'],
                         ipd_no=request.POST['ipd_no'],
                         death_date=request.POST['death_date'],
                         guardian_name=request.POST['guardian_name'],
                         message=request.POST['message'],
                         receiver_name=request.POST['receiver_name'])
    update12.save()
    easygui.msgbox("Data has been updated successfully!....")
    return redirect(admin_death)

def admin_death_delete(request,id):
    delete12=admin_deat.objects.get(id=id)
    delete12.delete()
    return redirect(admin_death)

def admin_staffD_edit(request,id):
    edit13=admin_staffD.objects.get(id=id)
    return render(request,'admin_staffD_edit.html',{'edit13':edit13})

def admin_staffD_update(request,id):
    update13=admin_staffD(id=id)
    update13.staff_id=request.POST.get('staff_id')
    update13.role=request.POST.get('role')
    update13.destination=request.POST.get('destination')
    update13.department=request.POST.get('department')
    update13.specialist=request.POST.get('specialist')
    update13.staff_first_name=request.POST.get('staff_first_name')
    update13.staff_last_name=request.POST.get('staff_last_name')
    update13.staff_father_name=request.POST.get('staff_father_name')
    update13.staff_mother_name=request.POST.get('staff_mother_name')
    update13.gender=request.POST.get('gender')
    update13.martial_status=request.POST.get('martial_status')
    update13.blood_grp=request.POST.get('blood_grp')
    update13.date=request.POST.get('date')
    update13.date_of_joining=request.POST.get('date_of_joining')
    update13.phone_no=request.POST.get('phone_no')
    update13.email=request.POST.get('email')
    update13.current_address=request.POST.get('current_address')
    update13.permanent_address=request.POST.get('permanent_address')

    if len(request.FILES) != 0:
            update13.staff_photo=request.FILES['staff_photo']
    
    update13.save()
    easygui.msgbox("Data has been updated Successfully!....")
    return redirect(admin_staffdetails)

def admin_staffD_delete(request,id):
    delete13=admin_staffD.objects.get(id=id)
    delete13.delete()
    return redirect(admin_staffdetails)

def admin_bedli_edit(request,id):
    edit14=admin_bed_lis.objects.get(id=id)
    return render(request,'admin_bedli_edit.html',{'edit14':edit14})

def admin_bedli_update(request,id):
    update14=admin_bed_lis(id=id)
    update14.name=request.POST['name']
    update14.bed_type=request.POST['bed_type']
    update14.bed_grp=request.POST['bed_grp']
    update14.status=request.POST['status']
    update14.save()
    easygui.msgbox("Data has been updated successfully!....")
    return redirect(admin_bedlist)

def admin_bedli_delete(request,id):
    delete14=admin_bed_lis.objects.get(id=id)
    delete14.delete()
    return redirect(admin_bedlist)

def admin_beds_edit(request,id):
    edit15=admin_bed_stat.objects.get(id=id)
    return render(request,'admin_beds_edit.html',{'edit15':edit15})

def admin_beds_update(request,id):
    update15=admin_bed_stat(id=id,number=request.POST['number'],
                             name=request.POST['name'],
                             bed_type=request.POST['bed_type'],
                             bed_grp=request.POST['bed_grp'],
                             status=request.POST['status'])
    update15.save()
    return redirect(admin_bedstatus)

def admin_beds_delete(request,id):
    delete15=admin_bed_stat.objects.get(id=id)
    delete15.delete()
    return redirect(admin_bedstatus)

def admin_profile_edit_DB(request):
    if request.method=='POST':
        edit15=admin_profile_edi()
        edit15.patient_id=request.POST.get('patient_id')
        edit15.gender=request.POST.get('gender')
        edit15.martial_status=request.POST.get('martial_status')
        edit15.phone=request.POST.get('phone')
        edit15.email=request.POST.get('email')
        edit15.address=request.POST.get('address')
        edit15.age=request.POST.get('age')
        edit15.guard_name=request.POST.get('guard_name')
        if len(request.FILES) != 0:
            edit15.profile_pic=request.FILES['profile_pic']
        edit15.save()
        easygui.msgbox("Your Profile has been updated!....")
        return redirect(admin_profile)

def admin_pharmacy_edit(request,id):
    edit16=admin_phar.objects.get(id=id)
    return render(request,'admin_pharmacy_edit.html',{'edit16':edit16})

def admin_pharmacy_update(request,id):
    update16=admin_phar(id=id,bill_no=request.POST['bill_no'],
                         date=request.POST['date'],
                         pat_name=request.POST['pat_name'],
                         doctor=request.POST['doctor'],
                         total=request.POST['total'])
    update16.save()
    easygui.msgbox("Data has been Updated Successfully!....")
    return redirect(admin_pharmacy)

def admin_pharmacy_delete(request,id):
    delete16=admin_phar.objects.get(id=id)
    delete16.delete()
    return redirect(admin_pharmacy)

def register_DB(request):
    if request.method=='POST':
        var1=reg(first_name=request.POST['first_name'],
                 username=request.POST['username'],
                 last_name=request.POST['lastname'],
                 password=request.POST['password'],
                 department=request.POST['department'])
        var1.save()

        subject = 'Registration Successfull!..'
        message = 'Welcome to Medicelab, Your regitration has been successfully Completed'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('department')
        print(recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)

        easygui.msgbox('Registartion Successful')
        return redirect(Userlogin)
    return render(request,'registerpage.html')

def admin_register_DB(request):
    if request.method=='POST':
        var14=admin_reg(first_name=request.POST['first_name'],
                 username=request.POST['username'],
                 last_name=request.POST['lastname'],
                 password=request.POST['password'],)
        var14.save()
        easygui.msgbox('Registartion Successful')
        return redirect(adminlogin)
    return render(request,'Admin-reg.html')


def login_auth(request):
    if request.method=='POST':
        if reg.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            ex1=reg.objects.get(username=request.POST['username'], password=request.POST['password'])
            global multi_user_name
            global user_current_password
            global user_current_id
            multi_user_name=ex1.username
            user_current_password=ex1.password
            user_current_id=ex1.id
            ut_data=reg.objects.get(username=multi_user_name)
            curr_pass=reg.objects.get(password=user_current_password)
            curr_id=reg.objects.get(id=user_current_id)
            easygui.msgbox('Login Successfull',title='Login_Form_Validate')
            return redirect(user_appoint)
        else:
            context={'msg':'You Entered Invalid Username or Password'}
            return render(request,'Loginpage.html',context)
    return render(request,'Loginpage.html')


def admin_login_auth(request):
    if request.method=='POST':
        if admin_reg.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            ex2=admin_reg.objects.get(username=request.POST['username'], password=request.POST['password'])
            global admin_multi_user_name
            global admin_current_password
            global admin_current_id
            admin_multi_user_name=ex2.username
            admin_current_password=ex2.password
            admin_current_id=ex2.id
            data=admin_reg.objects.get(username=admin_multi_user_name)
            a_curr_pass=admin_reg.objects.get(password=admin_current_password)
            a_curr_id=admin_reg.objects.get(id=admin_current_id)
            easygui.msgbox('Login Successfull',title='Login_Form_Validate')
            return redirect(admin_dash)
        else:
            easygui.msgbox('Login Failed(Invalid Username or Password)')
            return render(request,'Admin.html')
    return render(request,'Admin.html')

def admin_appoint_DB(request):
    if request.method=='POST':
        var2=admin_appoint_model(name=request.POST['name'],
                                 date=request.POST['date'],
                                 gender=request.POST['gender'],
                                 doctor=request.POST['doctor'],
                                 phone=request.POST['phone'],
                                 email=request.POST['email'],
                                 appoint_prio=request.POST['app_prio'],
                                 message=request.POST['message'],
                                 live_cons=request.POST['live_cons'])
        var2.save()

        subject = 'Appointment Added Successfully!..'
        message = 'Your appointment added successfully....:-)'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print(recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)

        easygui.msgbox('Data are stored Successfully!....')
        return redirect(admin_appointdetails)
    return render(request,'AppointDetails.html')

def admin_visitor_DB(request):
    if request.method=='POST':
        var3=admin_visitor_model(name=request.POST['name'],
                                 date=request.POST['date'],
                                 purpose=request.POST['purpose'],
                                 phone=request.POST['phone'],
                                 id_card=request.POST['id_card'],
                                 no_of_per=request.POST['no_of_per'],
                                 in_time=request.POST['in_time'],
                                 out_time=request.POST['out_time'],
                                 message=request.POST['message'])
        if len(request.FILES) != 0:
            var3.attach_document=request.FILES['attach_document']
        var3.save()
        easygui.msgbox('Data has been stored successfully!...')
        return redirect(admin_visitor)
    return render(request,'VisitorPage.html')

def admin_opd_DB(request):
    if request.method=='POST':
        var4=admin_opd(name=request.POST['name'],
                       guard_name=request.POST['guard_name'],
                       age=request.POST['age'],
                       date=request.POST['date'],
                       gender=request.POST['gender'],
                       blood_grp=request.POST['blood_grp'],
                       martial_status=request.POST['martial_status'],
                       phone=request.POST['phone'],
                       email=request.POST['email'],
                       address=request.POST['address'],
                       remarks=request.POST['remarks'],
                       message=request.POST['message'])
        if len(request.FILES) != 0:
            var4.pat_photo=request.FILES['pat_photo']
            var4.report=request.FILES['report']
        var4.save()
        easygui.msgbox('Data has been stored successfully!....')
        return redirect(admin_OPD)
    return render(request,'OPD.html')

def admin_ipd_DB(request):
    if request.method=='POST':
        var5=admin_ipd(name=request.POST['name'],
                       guard_name=request.POST['guard_name'],
                       age=request.POST['age'],
                       date=request.POST['date'],
                       gender=request.POST['gender'],
                       blood_grp=request.POST['blood_grp'],
                       martial_status=request.POST['martial_status'],
                       phone=request.POST['phone'],
                       email=request.POST['email'],
                       address=request.POST['address'],
                       remarks=request.POST['remarks'],
                       message=request.POST['message'])
        if len(request.FILES) != 0:
            var5.pat_photo=request.FILES['pat_photo']
            var5.report=request.FILES['report']
        var5.save()
        easygui.msgbox('Data has been stored successfully!....')
        return redirect(admin_IPD)
    return render(request,'IPD.html')

def admin_pharmedi_DB(request):
    if request.method=='POST':
        var6=admin_medi(medi_name=request.POST['medi_name'],
                            medi_cate=request.POST['medi_cate'],
                            medi_comp=request.POST['medi_comp'],
                            medi_composition=request.POST['medi_composition'],
                            medi_grp=request.POST['medi_grp'],
                            min_level=request.POST['min_level'],
                            re_order_level=request.POST['re_order_level'],
                            unit=request.POST['unit'],
                            vat=request.POST['vat'],
                            vat_AC=request.POST['vat_AC'],
                            message=request.POST['message'])
        if len(request.FILES) != 0:
            var6.medi_photo=request.FILES['medi_photo']
        var6.save()
        easygui.msgbox('Data has been stored successfully!..')
        return redirect(admin_pharmacy_medicine)
    return render(request,'Pharmacy-Medicine.html')

def admin_phar_DB(request):
    if request.method=='POST':
        var25=admin_phar(bill_no=request.POST['bill_no'],
                         date=request.POST['date'],
                         pat_name=request.POST['pat_name'],
                         doctor=request.POST['doctor'],
                         total=request.POST['total'])
        var25.save()
        easygui.msgbox("Data has been Stored Successfully!....")
        return redirect(admin_pharmacy)

def admin_pathotest_DB(request):
    if request.method=='POST':
        var7=admin_patho_test(test_name=request.POST['test_name'],
                              short_name=request.POST['short_name'],
                              test_type=request.POST['test_type'],
                              category_name=request.POST['category_name'],
                              sub_category=request.POST['sub_category'],
                              method=request.POST['method'],
                              report_daya=request.POST['report_days'],
                              charge_cate=request.POST['charge_cate'],
                              code=request.POST['code'],
                              std_charge=request.POST['std_charge'],
                              test_para_name=request.POST['test_para_name'],
                              ref_range=request.POST['ref_range'],
                              unit=request.POST['unit'])
        if len(request.FILES) != 0:
            var7.report=request.FILES['report']                   
        var7.save()
        easygui.msgbox('Data has been stored successfully!...')
        return redirect(admin_pathology)
    return render(request,'Pathology-Test.html')

def admin_radiotest_DB(request):
    if request.method=='POST':
        var8=admin_radio_test(test_name=request.POST['test_name'],
                              short_name=request.POST['short_name'],
                              test_type=request.POST['test_type'],
                              category_name=request.POST['category_name'],
                              sub_category=request.POST['sub_category'],
                              method=request.POST['method'],
                              report_daya=request.POST['report_days'],
                              charge_cate=request.POST['charge_cate'],
                              code=request.POST['code'],
                              std_charge=request.POST['std_charge'],
                              test_para_name=request.POST['test_para_name'],
                              ref_range=request.POST['ref_range'],
                              unit=request.POST['unit'])
        if len(request.FILES) != 0:
            var8.report=request.FILES['report'] 
        var8.save()
        easygui.msgbox('Data has been stored successfully!...')
        return redirect(admin_radiology)
    return render(request,'Radiology-Test.html')

def admin_operation_DB(request):
    if request.method=='POST':
        var9=admin_opeartionthea()
        var9.patient_name=request.POST['patient_name']
        var9.patient_id=request.POST['patient_id']
        var9.opeartion_date=request.POST['operation_date']
        var9.gender=request.POST['gender']
        var9.phone=request.POST['phone']
        var9.operation_name=request.POST['operation_name']
        var9.operation_type=request.POST['operation_type']
        var9.consultant=request.POST['consultant']
        var9.applied_charge=request.POST['applied_charge']
        var9.message=request.POST['message']
            
        if len(request.FILES) != 0:
            var9.attach_document=request.FILES['attach_document']
        var9.save()
        easygui.msgbox('Data has been stored successfully!...')
        return redirect(admin_OT)
    return render(request,'OperationTheatre.html')

def admin_blood_bank_DB(request):
    if request.method=='POST':
        var10=admin_blood_bank(blood_type=request.POST['blood_type'],
                               item=request.POST['item'],
                               supplier=request.POST['supplier'],
                               store=request.POST['store'],
                               quantity=request.POST['quantity'],
                               purchase_price=request.POST['purchase_price'],
                               date=request.POST['date'],
                               description=request.POST['description'],
                               donar_name=request.POST['donar_name'])
        var10.save()
        easygui.msgbox('Data has been stored successfully!...')
        return redirect(admin_blood)
    return render(request,'BloodBank.html')

def admin_ambu_DB(request):
    if request.method=='POST':
        var11=admin_ambul(vechile_number=request.POST['vechile_number'],
                          vechile_models=request.POST['vechile_model'],
                          year_made=request.POST['year_made'],
                          driver_name=request.POST['driver_name'],
                          driver_license=request.POST['driver_license'],
                          driver_contact=request.POST['driver_contact'],
                          vechile_type=request.POST['vechile_type'],
                          note=request.POST['note'])
        var11.save()
        easygui.msgbox('Data has been stored successfully!...')
        return redirect(admin_ambulance)
    return render(request,'Ambulance.html')

def admin_birth_DB(request):
    if request.method=='POST':
        var12=admin_birt()
        var12.child_name=request.POST.get('child_name')
        var12.gender=request.POST.get('gender')
        var12.weight=request.POST.get('weight')
        var12.birth_date=request.POST.get('birth_date')
        var12.phone=request.POST.get('phone')
        var12.address=request.POST.get('address')
        var12.father_name=request.POST.get('father_name')
        var12.mother_name=request.POST.get('mother_name')
        var12.ipd_no=request.POST.get('ipd_no')
        var12.report=request.POST.get('report')

        if len(request.FILES) != 0:
            var12.child_photo=request.FILES['child_photo']
            var12.father_photo=request.FILES['father_photo']
            var12.mother_photo=request.FILES['mother_photo']
            var12.attach_document=request.FILES['attach_document']
        
        var12.save()
        easygui.msgbox('Data has been stored successfully!...')
        return redirect(admin_birth)
    return render(request,'Birth.html')

def admin_death_DB(request):
    if request.method=='POST':
        var13=admin_deat(patient_name=request.POST['patient_name'],
                         ipd_no=request.POST['ipd_no'],
                         death_date=request.POST['death_date'],
                         guardian_name=request.POST['guardian_name'],
                         message=request.POST['message'],
                         receiver_name=request.POST['receiver_name'])
        var13.save()
        easygui.msgbox('Data has been stored successully!....')
        return redirect(admin_death)
    return render(request,'Death.html')

def admin_staffD_DB(request):
    if request.method=='POST':
        var18=admin_staffD()
        var18.staff_id=request.POST.get('staff_id')
        var18.role=request.POST.get('role')
        var18.destination=request.POST.get('destination')
        var18.department=request.POST.get('department')
        var18.specialist=request.POST.get('specialist')
        var18.staff_first_name=request.POST.get('staff_first_name')
        var18.staff_last_name=request.POST.get('staff_last_name')
        var18.staff_father_name=request.POST.get('staff_father_name')
        var18.staff_mother_name=request.POST.get('staff_mother_name')
        var18.gender=request.POST.get('gender')
        var18.martial_status=request.POST.get('martial_status')
        var18.blood_grp=request.POST.get('blood_grp')
        var18.date=request.POST.get('date')
        var18.date_of_joining=request.POST.get('date_of_joining')
        var18.phone_no=request.POST.get('phone_no')
        var18.email=request.POST.get('email')
        var18.current_address=request.POST.get('current_address')
        var18.permanent_address=request.POST.get('permanent_address')

        if len(request.FILES) != 0:
            var18.staff_photo=request.FILES['staff_photo']
        
        var18.save()
        easygui.msgbox('Data has been stored successully!....')
        return redirect(admin_staffdetails)
    return render(request,'StaffDetails.html')

def admin_bed_list_DB(request):
    if request.method=='POST':
        var19=admin_bed_lis()
        var19.name=request.POST['name']
        var19.bed_type=request.POST['bed_type']
        var19.bed_grp=request.POST['bed_grp']
        var19.status=request.POST['status']
        var19.save()
        easygui.msgbox("Your data has been stored successully!..")
        return redirect(admin_bedlist)
    return render(request,'BedList.html')

def admin_bed_status_DB(request):
    if request.method=='POST':
        var20=admin_bed_stat(number=request.POST['number'],
                             name=request.POST['name'],
                             bed_type=request.POST['bed_type'],
                             bed_grp=request.POST['bed_grp'],
                             status=request.POST['status'])
        var20.save()
        easygui.msgbox("Data has been stored successfully!..")
        return redirect(admin_bedstatus)

def landing_form_DB(request):
    if request.method=='POST':
        var14=landing_form(name=request.POST['name'],
                           email=request.POST['email'],
                           phone=request.POST['phone'],
                           date=request.POST['date'],
                           department=request.POST['department'],
                           doctor=request.POST['doctor'],
                           message=request.POST['message'])
        var14.save()

        subject = 'Appointment Added Successfully!..'
        message = 'Your appointment added successfully....:-)'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print(recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)

        easygui.msgbox('Appointment successfully added!...you will receive mail regarding this...')
        return redirect(index)

def landing_feedback_form_DB(request):
    if request.method=='POST':
        var16=landing_feedback_form(name=request.POST['name'],
                                    email=request.POST['email'],
                                    subject=request.POST['subject'],
                                    message=request.POST['message'])
        var16.save()
        easygui.msgbox('Thanks For your response!...',title='FeedBack')
        return redirect(index)

    return render(request,'index.html')

def user_appoint_DB(request):
    if request.method=='POST':
        var15=user_appoin(name=request.POST['name'],
                          date=request.POST['date'],
                          gender=request.POST['gender'],
                          doctor=request.POST['doctor'],
                          phone=request.POST['phone'],
                          email=request.POST['email'],
                          appoint_prio=request.POST['app_prio'],
                          message=request.POST['message'],
                          live_cons=request.POST['live_cons'])
        var15.save()

        subject = 'Appointment Added Successfully!..'
        message = 'Your appointment added successfully....:-)'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print(recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)

        easygui.msgbox('Appointment successfully added!....')
        return redirect(user_appoint)
    return render(request,'User-AppointDetails.html')

def user_appoint_edit(request,id):
    edit3=user_appoin.objects.get(id=id)
    return render(request,'user_app_edit.html',{'edit3':edit3})

def user_appoint_update(request,id):
    update3=user_appoin(id=id,name=request.POST['name'],
                          date=request.POST['date'],
                          gender=request.POST['gender'],
                          doctor=request.POST['doctor'],
                          phone=request.POST['phone'],
                          email=request.POST['email'],
                          appoint_prio=request.POST['app_prio'],
                          message=request.POST['message'],
                          live_cons=request.POST['live_cons'])
    update3.save()
    easygui.msgbox('your data has been updated successfully!...',title='UPDATE')
    return redirect(user_appoint)

def user_appoint_delete(request,id):
    delete3=user_appoin.objects.get(id=id)
    delete3.delete()
    easygui.msgbox('Your data has been Deleted...')
    return redirect(admin_appointdetails)

def user_livecons_DB(request):
    if request.method=='POST':
        var16=user_liveco(pat_id=request.POST['pat_id'],
                           pat_name=request.POST['pat_name'],
                           email=request.POST['email'],
                           phone=request.POST['phone'],
                           live_cons=request.POST['live_cons'])
        var16.save()
        easygui.msgbox("Data has been Stored Successfully!....")
        return redirect(user_livecons)

def need_blood_DB(request):
    if request.method=='POST':
        var17=need_bloo(blood_type=request.POST['blood_type'],
                        blood_priority=request.POST['blood_priority'])
        var17.save()
        easygui.msgbox("Data has been successfully send!...")
        return redirect(admin_blood)
    return render(redirect,'BloodBank.html')

def user_profile_edit_DB(request):
    if request.method=='POST':
        edit15=user_profile_edi()
        edit15.patient_id=request.POST.get('patient_id')
        edit15.gender=request.POST.get('gender')
        edit15.martial_status=request.POST.get('martial_status')
        edit15.phone=request.POST.get('phone')
        edit15.email=request.POST.get('email')
        edit15.address=request.POST.get('address')
        edit15.age=request.POST.get('age')
        edit15.guard_name=request.POST.get('guard_name')
        if len(request.FILES) != 0:
            edit15.profile_pic=request.FILES['profile_pic']
        edit15.save()
        easygui.msgbox("Your Profile has been updated!....")
        return redirect(user_profile)

def user_pharmacy_order_DB(request):
    if request.method=='POST':
        var26=order_medic(pat_id=request.POST['pat_id'],
                          name=request.POST['name'],
                          age=request.POST['age'],
                          gender=request.POST['gender'],
                          blood_grp=request.POST['blood_grp'],
                          phone=request.POST['phone'],
                          email=request.POST['email'],
                          address=request.POST['address'],
                          medi_name=request.POST['medi_name'],
                          quantity=request.POST['quantity'])
        var26.save()
        easygui.msgbox("Your Order has been Placed!....")
        return redirect(user_pharmacy)

def admin_message_DB(request):
    if request.method=='POST':
        var27=admin_mess(pat_id=request.POST['pat_id'],
                         message=request.POST['message'])
        var27.save()
        easygui.msgbox("Your Message has been send Successfully")
        return redirect(admin_message)

def user_complete_profile_DB(request):
    if request.method=='POST':
        edit15=user_com_pro()
        edit15.gender=request.POST.get('gender')
        edit15.martial_status=request.POST.get('martial_status')
        edit15.phone=request.POST.get('phone')
        edit15.email=request.POST.get('email')
        edit15.address=request.POST.get('address')
        edit15.age=request.POST.get('age')
        edit15.guard_name=request.POST.get('guard_name')
        if len(request.FILES) != 0:
            edit15.profile_pic=request.FILES['profile_pic']
        edit15.save()
        easygui.msgbox("Your Profile has been updated!....")
        return redirect(user_profile)
    
def landing_form_edit(request,id):
    edit25=landing_form.objects.get(id=id)
    return render(request,'landing_form_edit.html',{'edit25':edit25})

def landing_form_update(request,id):
    update25=landing_form(id=id,name=request.POST['name'],
                           email=request.POST['email'],
                           phone=request.POST['phone'],
                           date=request.POST['date'],
                           department=request.POST['department'],
                           doctor=request.POST['doctor'],
                           message=request.POST['message'])
    update25.save()
    easygui.msgbox("Data has been Updated")
    return redirect(admin_appointdetails)

def landing_form_delete(request,id):
    delete25=landing_form.objects.get(id=id)
    delete25.delete()
    return redirect(admin_appointdetails)

def logout(request):
    log(request)
    easygui.msgbox('Logged out Successfully')
    return render(request,'Admin.html')

def user_logout(request):
    log(request)
    easygui.msgbox("Logged out Successfully!...")
    return render(request,'Loginpage.html')