from django.contrib import admin
from . models import admin_mess, admin_phar, admin_profile_edi, messages, need_bloo, order_medic, reg,admin_appoint_model,user_appoin,admin_staffD,landing_feedback_form,landing_form,admin_reg,admin_visitor_model,admin_opd,admin_ipd,admin_medi,admin_patho_test,admin_radio_test,admin_opeartionthea,admin_blood_bank,admin_ambul,admin_birt,admin_deat,admin_bed_lis,admin_bed_stat, user_com_pro, user_liveco, user_profile_edi

# Register your models here.
admin.site.register(reg)
admin.site.register(admin_reg)
admin.site.register(admin_appoint_model)
admin.site.register(admin_visitor_model)
admin.site.register(admin_opd)
admin.site.register(admin_ipd)
admin.site.register(admin_medi)
admin.site.register(admin_patho_test)
admin.site.register(admin_radio_test)
admin.site.register(admin_opeartionthea)
admin.site.register(admin_blood_bank)
admin.site.register(admin_ambul)
admin.site.register(admin_birt)
admin.site.register(admin_deat)
admin.site.register(landing_form)
admin.site.register(user_appoin)
admin.site.register(landing_feedback_form)
admin.site.register(admin_staffD)
admin.site.register(admin_bed_lis)
admin.site.register(admin_bed_stat)
admin.site.register(admin_profile_edi)
admin.site.register(admin_phar)
admin.site.register(user_liveco)
admin.site.register(messages)
admin.site.register(need_bloo)
admin.site.register(user_profile_edi)
admin.site.register(order_medic)
admin.site.register(admin_mess)
admin.site.register(user_com_pro)