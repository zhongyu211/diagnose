from django.contrib import admin
from diagnose_app.models import SDM_MEAS_HSS_CX
from diagnose_app.models import SDM_MEAS_HSS_SH
from diagnose_app.models import SDM_MEAS_HSS_CX_SAR
from diagnose_app.models import SDM_MEAS_HSS_CX_MIX
from diagnose_app.models import SDM_MEAS_HSS_SHHD
from diagnose_app.models import SDM_MEAS_HSS_NOTIF_EFF
from diagnose_app.models import SDM_MEAS_HSS_CX_PRSET
from diagnose_app.models import SDM_MEAS_SH_NE9
from diagnose_app.models import SDM_MEAS_HSS_PSI_CX
from diagnose_app.models import SDM_MEAS_HSS_PSI_SH
from diagnose_app.models import SDM_MEAS_IMS_SLF
from diagnose_app.models import SDM_MEAS_IMS_MSG_LATENCY
from diagnose_app.models import SDM_MEAS_HSS_ACCT
from diagnose_app.models import SDM_MEAS_HSS_ZH
from diagnose_app.models import SDM_MEAS_MAP_IMS
from diagnose_app.models import SDM_MEAS_HSS_SH_IDSET
from diagnose_app.models import SDM_MEAS_HSS_MIX
from diagnose_app.models import SDM_MEAS_SH_NE1
from diagnose_app.models import SDM_MEAS_SH_NE2
from diagnose_app.models import SDM_MEAS_SH_NE3
from diagnose_app.models import SDM_MEAS_SH_NE4
from diagnose_app.models import SDM_MEAS_SH_NE5
from diagnose_app.models import SDM_MEAS_SH_NE6
from diagnose_app.models import SDM_MEAS_SH_NE7
from diagnose_app.models import SDM_MEAS_SH_NE8
from diagnose_app.models import SDM_MEAS_SH_NE10
from diagnose_app.models import SDM_MEAS_SH_NE11
from diagnose_app.models import SDM_MEAS_SH_NE12
from diagnose_app.models import SDM_MEAS_SH_NE13
from diagnose_app.models import SDM_MEAS_SH_NE14
from diagnose_app.models import SDM_MEAS_SH_NE15
from diagnose_app.models import SDM_MEAS_SH_NE16
from diagnose_app.models import SDM_MEAS_SH_NE17
from diagnose_app.models import SDM_MEAS_SH_NE18
from diagnose_app.models import SDM_MEAS_SH_NE19
from diagnose_app.models import SDM_MEAS_SH_NE20
from diagnose_app.models import SDM_MEAS_HSSDROPLOG
from diagnose_app.models import SDM_MEAS_HSS_DMS
from diagnose_app.models import SDM_MEAS_HSS_SWX
from diagnose_app.models import SDM_MEAS_SWX_SAR
from diagnose_app.models import SDM_MEAS_SWX_IN
from diagnose_app.models import SDM_MEAS_S6A_IN
from diagnose_app.models import SDM_MEAS_S6A_OUT
from diagnose_app.models import SDM_MEAS_LTE_MIX
from diagnose_app.models import SDM_MEAS_S6A_AIR
from diagnose_app.models import SDM_MEAS_LTEDROPLOG
from diagnose_app.models import SDM_MEAS_LTE_MSG_LATENCY
from diagnose_app.models import SDM_MEAS_EIR_S13
from diagnose_app.models import SDM_MEAS_UMTS_ACR
from diagnose_app.models import SDM_MEAS_UMTS_AUTH
from diagnose_app.models import SDM_MEAS_UMTS_BLACKLIST
from diagnose_app.models import SDM_MEAS_UMTS_DROPLOG
from diagnose_app.models import SDM_MEAS_UMTS_GEN_FAIL
from diagnose_app.models import SDM_MEAS_UMTS_ICK
from diagnose_app.models import SDM_MEAS_UMTS_INTWK
from diagnose_app.models import SDM_MEAS_UMTS_ISD_CS
from diagnose_app.models import SDM_MEAS_UMTS_ISD_PS
from diagnose_app.models import SDM_MEAS_UMTS_LCN
from diagnose_app.models import SDM_MEAS_UMTS_LOC_UPD
from diagnose_app.models import SDM_MEAS_UMTS_MISC
from diagnose_app.models import SDM_MEAS_UMTS_MSG_MIX
from diagnose_app.models import SDM_MEAS_UMTS_MSG_MIX2
from diagnose_app.models import SDM_MEAS_UMTS_MSG_MIX3
from diagnose_app.models import SDM_MEAS_UMTS_MSG_REJ
from diagnose_app.models import SDM_MEAS_UMTS_MSRN
from diagnose_app.models import SDM_MEAS_UMTS_ODB
from diagnose_app.models import SDM_MEAS_UMTS_PREPAY
from diagnose_app.models import SDM_MEAS_UMTS_SMS
from diagnose_app.models import SDM_MEAS_UMTS_SRI
from diagnose_app.models import SDM_MEAS_UMTS_SRI_VM
from diagnose_app.models import SDM_MEAS_UMTS_SS_FAIL
from diagnose_app.models import SDM_MEAS_UMTS_SS1
from diagnose_app.models import SDM_MEAS_UMTS_SS2
from diagnose_app.models import SDM_MEAS_UMTS_TCC
from diagnose_app.models import SDM_MEAS_UMTS_USSD
from diagnose_app.models import SDM_MEAS_EIR
from diagnose_app.models import SDM_MEAS_UMTS_USSD_FWD
from diagnose_app.models import SDM_MEAS_UMTS_USSD_RELAY
from diagnose_app.models import SDM_MEAS_UMTS_SAI_DYNAMIC
from diagnose_app.models import SDM_MEAS_UMTS_VOICEMAIL
from diagnose_app.models import SDM_MEAS_LOAD_STATION_HLT
from diagnose_app.models import SDM_MEAS_LOAD_STATION_LTE
from diagnose_app.models import SDM_MEAS_LOAD_STATION_HSS
from diagnose_app.models import SDM_MEAS_UMTS_FPLMN_ADDRESS
from diagnose_app.models import SDM_MEAS_UMTS_HPLMN_ADDRESS
from diagnose_app.models import SDM_MEAS_HLR_TCAP
from diagnose_app.models import SDM_MEAS_LTE_SA_PDN
from diagnose_app.models import SDM_MEAS_S6D_IN
from diagnose_app.models import SDM_MEAS_S6D_AIR
from diagnose_app.models import SDM_MEAS_HLR_OUT_REJ
from diagnose_app.models import SDM_MEAS_LTE_OUT_REJ
from diagnose_app.models import SDM_MEAS_HSS_OUT_REJ
from diagnose_app.models import SDM_MEAS_SLH_IN
from diagnose_app.models import SDM_MEAS_SLH_OUT
from diagnose_app.models import SDM_MEAS_HLR_BE_IN
from diagnose_app.models import SDM_MEAS_MNP_MSG_MIX1
from diagnose_app.models import SDM_MEAS_MNP_MSG_MIX2
from diagnose_app.models import SDM_MEAS_MNP_MSG_MIX3
from diagnose_app.models import SDM_MEAS_MNP_CALL
from diagnose_app.models import SDM_MEAS_MNP_MSG_REJ
from diagnose_app.models import SDM_MEAS_MNP_BLACKLIST
from diagnose_app.models import SDM_MEAS_MNP_DROPLOG
from diagnose_app.models import SDM_MEAS_LOAD_STATION_MNP
# Register your models here.
admin.site.register(SDM_MEAS_HSS_CX)
admin.site.register(SDM_MEAS_HSS_SH)
admin.site.register(SDM_MEAS_HSS_CX_SAR)
admin.site.register(SDM_MEAS_HSS_CX_MIX)
admin.site.register(SDM_MEAS_HSS_SHHD)
admin.site.register(SDM_MEAS_HSS_NOTIF_EFF)
admin.site.register(SDM_MEAS_HSS_CX_PRSET)
admin.site.register(SDM_MEAS_SH_NE9)
admin.site.register(SDM_MEAS_HSS_PSI_CX)
admin.site.register(SDM_MEAS_HSS_PSI_SH)
admin.site.register(SDM_MEAS_IMS_SLF)
admin.site.register(SDM_MEAS_IMS_MSG_LATENCY)
admin.site.register(SDM_MEAS_HSS_ACCT)
admin.site.register(SDM_MEAS_HSS_ZH)
admin.site.register(SDM_MEAS_MAP_IMS)
admin.site.register(SDM_MEAS_HSS_SH_IDSET)
admin.site.register(SDM_MEAS_HSS_MIX)
admin.site.register(SDM_MEAS_SH_NE1)
admin.site.register(SDM_MEAS_SH_NE2)
admin.site.register(SDM_MEAS_SH_NE3)
admin.site.register(SDM_MEAS_SH_NE4)
admin.site.register(SDM_MEAS_SH_NE5)
admin.site.register(SDM_MEAS_SH_NE6)
admin.site.register(SDM_MEAS_SH_NE7)
admin.site.register(SDM_MEAS_SH_NE8)
admin.site.register(SDM_MEAS_SH_NE10)
admin.site.register(SDM_MEAS_SH_NE11)
admin.site.register(SDM_MEAS_SH_NE12)
admin.site.register(SDM_MEAS_SH_NE13)
admin.site.register(SDM_MEAS_SH_NE14)
admin.site.register(SDM_MEAS_SH_NE15)
admin.site.register(SDM_MEAS_SH_NE16)
admin.site.register(SDM_MEAS_SH_NE17)
admin.site.register(SDM_MEAS_SH_NE18)
admin.site.register(SDM_MEAS_SH_NE19)
admin.site.register(SDM_MEAS_SH_NE20)
admin.site.register(SDM_MEAS_HSSDROPLOG)
admin.site.register(SDM_MEAS_HSS_DMS)
admin.site.register(SDM_MEAS_HSS_SWX)
admin.site.register(SDM_MEAS_SWX_SAR)
admin.site.register(SDM_MEAS_SWX_IN)
admin.site.register(SDM_MEAS_S6A_IN)
admin.site.register(SDM_MEAS_S6A_OUT)
admin.site.register(SDM_MEAS_LTE_MIX)
admin.site.register(SDM_MEAS_S6A_AIR)
admin.site.register(SDM_MEAS_LTEDROPLOG)
admin.site.register(SDM_MEAS_LTE_MSG_LATENCY)
admin.site.register(SDM_MEAS_EIR_S13)
admin.site.register(SDM_MEAS_UMTS_ACR)
admin.site.register(SDM_MEAS_UMTS_AUTH)
admin.site.register(SDM_MEAS_UMTS_BLACKLIST)
admin.site.register(SDM_MEAS_UMTS_DROPLOG)
admin.site.register(SDM_MEAS_UMTS_GEN_FAIL)
admin.site.register(SDM_MEAS_UMTS_ICK)
admin.site.register(SDM_MEAS_UMTS_INTWK)
admin.site.register(SDM_MEAS_UMTS_ISD_CS)
admin.site.register(SDM_MEAS_UMTS_ISD_PS)
admin.site.register(SDM_MEAS_UMTS_LCN)
admin.site.register(SDM_MEAS_UMTS_LOC_UPD)
admin.site.register(SDM_MEAS_UMTS_MISC)
admin.site.register(SDM_MEAS_UMTS_MSG_MIX)
admin.site.register(SDM_MEAS_UMTS_MSG_MIX2)
admin.site.register(SDM_MEAS_UMTS_MSG_MIX3)
admin.site.register(SDM_MEAS_UMTS_MSG_REJ)
admin.site.register(SDM_MEAS_UMTS_MSRN)
admin.site.register(SDM_MEAS_UMTS_ODB)
admin.site.register(SDM_MEAS_UMTS_PREPAY)
admin.site.register(SDM_MEAS_UMTS_SMS)
admin.site.register(SDM_MEAS_UMTS_SRI)
admin.site.register(SDM_MEAS_UMTS_SRI_VM)
admin.site.register(SDM_MEAS_UMTS_SS_FAIL)
admin.site.register(SDM_MEAS_UMTS_SS1)
admin.site.register(SDM_MEAS_UMTS_SS2)
admin.site.register(SDM_MEAS_UMTS_TCC)
admin.site.register(SDM_MEAS_UMTS_USSD)
admin.site.register(SDM_MEAS_EIR)
admin.site.register(SDM_MEAS_UMTS_USSD_FWD)
admin.site.register(SDM_MEAS_UMTS_USSD_RELAY)
admin.site.register(SDM_MEAS_UMTS_SAI_DYNAMIC)
admin.site.register(SDM_MEAS_UMTS_VOICEMAIL)
admin.site.register(SDM_MEAS_LOAD_STATION_HLT)
admin.site.register(SDM_MEAS_LOAD_STATION_LTE)
admin.site.register(SDM_MEAS_LOAD_STATION_HSS)
admin.site.register(SDM_MEAS_UMTS_FPLMN_ADDRESS)
admin.site.register(SDM_MEAS_UMTS_HPLMN_ADDRESS)
admin.site.register(SDM_MEAS_HLR_TCAP)
admin.site.register(SDM_MEAS_LTE_SA_PDN)
admin.site.register(SDM_MEAS_S6D_IN)
admin.site.register(SDM_MEAS_S6D_AIR)
admin.site.register(SDM_MEAS_HLR_OUT_REJ)
admin.site.register(SDM_MEAS_LTE_OUT_REJ)
admin.site.register(SDM_MEAS_HSS_OUT_REJ)
admin.site.register(SDM_MEAS_SLH_IN)
admin.site.register(SDM_MEAS_SLH_OUT)
admin.site.register(SDM_MEAS_HLR_BE_IN)
admin.site.register(SDM_MEAS_MNP_MSG_MIX1)
admin.site.register(SDM_MEAS_MNP_MSG_MIX2)
admin.site.register(SDM_MEAS_MNP_MSG_MIX3)
admin.site.register(SDM_MEAS_MNP_CALL)
admin.site.register(SDM_MEAS_MNP_MSG_REJ)
admin.site.register(SDM_MEAS_MNP_BLACKLIST)
admin.site.register(SDM_MEAS_MNP_DROPLOG)
admin.site.register(SDM_MEAS_LOAD_STATION_MNP)
