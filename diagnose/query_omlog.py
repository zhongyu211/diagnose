from django.db.models import Q
from diagnose_app.models import *

class query_omlog:
	"""
	 this class use to query OMlog table based on conditions
	"""
	def __init__(self,startDay,startTime,endDay,endTime,matchList,tableName = 'OMLOG'):
		self.__tableName__ = tableName
		self.__startDay__ = startDay
		self.__startTime__ = startTime
		self.__endDay__ = endDay
		self.__endTime__ = endTime
		self.__matchList__ = matchList
		self.__querylist__ = [] 
		self.returnQueryList = []

	def query_duration(self):
		"""
		this function query all records between 'startDay startTime' and 'endDay endTime'			
		"""
		if self.__startDay__ == self.__endDay__ and self.__startTime__ == self.__endTime__:
			self.__querylist__ = (eval(self.__tableName__+".objects.filter(Q(Day__exact=self.__startDay__) & Q(Time__exact=self.__startTime__))"))
		elif self.__startDay__ == self.__endDay__ and self.__startTime__ != self.__endTime__:
			self.__querylist__ = (eval(self.__tableName__+".objects.filter(Q(Day__exact=self.__startDay__) & (Q(Time__gte=self.__startTime__) & Q(Time__lte=self.__endTime__)))"))
		else:
			self.__querylist__ = (eval(self.__tableName__+".objects.filter((Q(Day__gt=self.__startDay__) & Q(Day__lt=self.__endDay__)) | (Q(Day__exact=self.__startDay__) & Q(Time__gte=self.__startTime__)) | (Q(Day__exact=self.__endDay__) & Q(Time__lte=self.__endTime__)))"))
		
	def query_matchlist(self):
		"""
		this function query records which match the matchList 
		"""
		for match in self.__matchList__:
			self.__querylist__ = self.__querylist__.filter(DESCRIPTION__contains = match)
 		
	def query(self):
		"""
		this function store the query records into a list
		"""
		self.query_duration()
		self.query_matchlist()
		for record in self.__querylist__:
			temp_list = []
			temp_list.append(str(record.NODENAME))
			timeStamp = str(record.Day) + " " + str(record.Time)
			temp_list.append(timeStamp)
			temp_list.append(str(record.MSGCLASS))
			temp_list.append(str(record.BLADE))
			temp_list.append(str(record.TITLE))
			temp_list.append(str(record.DESCRIPTION))
			temp_list.append(str(record.LOG_ID))
			self.returnQueryList.append(temp_list)
 
		return self.returnQueryList
 

	

