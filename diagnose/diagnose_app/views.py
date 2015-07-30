from django.shortcuts import render_to_response
#from django.utils.httpwrappers import HttpResponse
from django.template import loader,Context
from django.http import HttpResponse
from diagnose_app.models import SDM_MEAS_HSS_SH
from django.db.models import get_app, get_models
from django.db import models
from django.db import connection
from django.utils import simplejson
from data_factory import *
from data_load import *
import json
import datetime
import pdb
import os
'''
def index(request):
    return HttpResponse()
# Create your views here.
'''
#show the main page
def index(req):
    sdm_meas_sh= SDM_MEAS_HSS_SH.objects.all()
    
    #current_date = datetime.datetime.now() 
    return render_to_response('index.html',locals())
def setting(req):
    return render_to_response('setting.html',{})
#the counts performance 
def counts(reqest):
    app = get_app('diagnose_app')
    models =get_models(app, include_auto_created=True)
    models_name= [model._meta.db_table for model in get_models(app, include_auto_created=True)]
	
    #err= names.SH_PNA_ERROR 
    return render_to_response('counts.html',{'models_name':models_name})
#the trafficload page    
def trafficload(req):
    return render_to_response('trafficload.html',{})
#teh trouble shooting page
def troubleshooting(req):
    return render_to_response('troubleshooting.html',{})
#the abnormal log page
def abnormal(req):
    return render_to_response('abnormal.html',{})

#get the distinct time, blade and counts name info
def gettableinfo(request,tablename):
    tableinfo={}
    datedis=[]
    bladedis = []
    counts = []
    if request.is_ajax():
        if request.method=='GET':
            for m in get_models(get_app('diagnose_app'), include_auto_created=True):
                if m._meta.db_table == request.GET.get('tablename'):
                    for bd in m.objects.values('STATION_ID').distinct():
                        bladedis.append(bd['STATION_ID'])
                    for dt in m.objects.values('Day','Time').distinct():
                        datedis.append(dt['Day'].isoformat()+' '+dt['Time'].isoformat())
                    for ct in m._meta.get_all_field_names():
                        if ct.isupper():
                            counts.append(ct)

                    #tableinfo.append(m._meta.get_field('Blade'))
                    tableinfo['tablename'] = request.GET.get('tablename')
                    tableinfo['blades'] = bladedis
                    tableinfo['times'] = datedis
                    tableinfo['counts'] = counts
                    #tableinfo=tableinfo.append('abcde')
                    #table_info_json=json.dumps(tableinfo)
                    table_info_json=json.dumps(tableinfo)
    return HttpResponse(table_info_json,content_type="application/json")            
#recieve the statistic info from the request and response the chart info
def getchartinfo(request):
    tablename = request.GET.get('table')
    blade=''
    blade = str(request.GET.get('blade')).split(',')

    blade.remove('')
    startdate = request.GET.get('starttime').split(" ")[0]
    starttime = request.GET.get('starttime').split(" ")[1]
    enddate = request.GET.get('endtime').split(" ")[0]
    endtime = request.GET.get('endtime').split(" ")[1]
    countlist = str(request.GET.get('counts')).split(",")
    countlist.remove('')
    data =  data_factory(tablename, startdate, starttime, enddate, endtime, blade, countlist)
    return HttpResponse(data.meaData_factory(),content_type="application/json")

#get the highest frequency LogId from DB

    #abc=json.dumps(['2015-03-02', '03:25:06', '2015-03-02'])
    #return HttpResponse(json.dumps(blade),content_type="application/json")
    #return HttpResponse(blade)
#get log data path
def prepdata(request):
    pathname=request.GET.get('logpath')
    dataload_status=""
    if os.path.isdir(pathname):

        load = data_load(pathname)
        dataload_status=load.load_file()
    else:
        dataload_status="The path not exist in server, please retry."
    return HttpResponse(dataload_status)
#diagnsoe 
def diagnose(request):
     
    return render_to_response('diagnose.html',{})
#tables
def tables(request):
    
    return render_to_response('tables.html',{})
    
#get logid test

def runquery(sql):
    row=[] 
    cursor = connection.cursor()
    row=cursor.execute(sql,None)
    return row
def getlogid(request):
    loginfo=[]
    logtmp={}
    cursor = connection.cursor()
    for m in get_models(get_app('diagnose_app'), include_auto_created=True):
        if m._meta.db_table == 'diagnose_app_omlog':
            cursor.execute("select LOG_ID, count(LOG_ID) from diagnose_app_omlog where LOG_ID > 1 group by LOG_ID order by count(LOG_ID) desc limit 0,10",None)
            logtmp=cursor.fetchall()
            for i in range(0,len(logtmp)):
                temp={}
                temp['log_id']=str(logtmp[i][0])
                temp['log_cnt']=int(logtmp[i][1])
                loginfo.append(temp)
    log_json=json.dumps(loginfo)
    return HttpResponse(log_json,content_type="application/json")

#get the highest frequency LogId from DB
def getdiagnoseinfo(request):
    tablename = request.GET.get('button')
    

    return HttpResponse(data.meaData_factory(),content_type="application/json")

    #abc=json.dumps(['2015-03-02', '03:25:06', '2015-03-02'])
    #return HttpResponse(json.dumps(blade),content_type="application/json")
    #return HttpResponse(blade)
