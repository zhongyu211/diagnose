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

    def my_query_table(self):
        """
        this function query data with class query_table
        """
        whole_list = self.counterList
        whole_list[0:0] = ['STATION_ID']
        table = self.tableName.split('diagnose_app_')[1].upper()
        print self.startdate, self.startTime, self.endDate, self.endTime
        data_query = query_table(table, self.startdate, self.startTime, self.endDate, self.endTime, whole_list)
        return data_query.query_list()

    def meaData_factory(self):
        """
        this function store the related info into returnList and return with json format
        returnlist = [time, blade, countdict]
        """
        countdict={}
        returnlist=[]
        datalist = self.my_query_table()
        #print datalist
        #return
        for data in datalist:
            time = data[0]
            blade = data[1]
            if blade not in self.bladeList:
                continue
            for i in range(2,len(data)):
                countdict[self.counterList[i-1]] = data[i]
            returnlist.append([time, blade, countdict])
        print returnlist
        return json.dumps(returnlist)
