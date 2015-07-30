import json
from query_table import *

class data_factory:
    """
    this class use to get data from DB and response to web server
    """
    def __init__(self,tableName,startDate,startTime,endDate,endTime,bladeList,counterList):
        self.tableName = tableName
        self.startdate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime
        self.bladeList = bladeList
        self.counterList = counterList

    def query_table(self):
        """
        this function query data with class query_table
        """
        whole_list = self.counterList
        whole_list[0:0] = ['STATION_ID']
        table = self.tableName.split('diagnose_app_')[1].upper()
        data_query = query_table(table, self.startdate, self.startTime, self.endDate, self.endTime, whole_list)
        return data_query.query_list()

    def meaData_factory(self):
        """
        this function store the related info into returnList and return with json format
        returnlist = [time, blade, countdict]
        """
        countdict={}
        returnlist=[]
        datalist = self.query_table()
        for data in datalist:
            time = data[0]
            blade = data[1]
            if blade not in self.bladeList:
                continue
            for i in range(2,len(data)):
                countdict[self.counterList[i-1]] = data[i]
            returnlist.append([time, blade, countdict])
        return json.dumps(self.parselist(returnlist))
#parse the counts data from list to dic 
    def parselist(self, listdata):
        """parse list"""
        datadic={}
        blades=[]
        times=[]
        for d in listdata:
            d[1]=str(d[1])
            for k in d[2].keys():
                d[2][k]=int(d[2][k])
                
            if not d[1] in blades:
                blades.append(str(d[1]))
            if not d[0] in times:
                times.append(d[0])
                
        #exam={blade:{time1:{}}}        
        countinfo=[]

        for b in blades:
            ct={}
            ct['countname']=[]
            ct['blade']=b
            ct['countsinfo']=[]

            for d in listdata:
                if d[1]==b:
                    ct['countname']=d[2].keys()
                    cinfo={}
                    cinfo['timestamp']=d[0]
                    cinfo=dict(cinfo.items()+d[2].items())
                    ct['countsinfo'].append(cinfo)
            countinfo.append(ct)
        return countinfo
