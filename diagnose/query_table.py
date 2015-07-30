from diagnose_app.models import *

class query_table:
	"""
	 this class use to query table based on conditions
	"""
	def __init__(self,tableName,startDay,startTime,endDay,endTime,counterList):
		self.__tableName__ = tableName
		self.__startDay__ = startDay
		self.__startTime__ = startTime
		self.__endDay__ = endDay
		self.__endTime__ = endTime
		self.__counterList__ = counterList
		self.__querylist__ = [] 
		self.returnQueryList = []

	def query(self):
		"""
		this function query all records between 'startDay startTime' and 'endDay endTime'			
		"""
		if self.__startDay__ == self.__endDay__ and self.__startTime__ == self.__endTime__:
			self.__querylist__.extend(eval(self.__tableName__+".objects.filter(Day__exact=self.__startDay__).filter(Time__exact=self.__startTime__)"))
		elif self.__startDay__ == self.__endDay__ and self.__startTime__ != self.__endTime__:
			self.__querylist__.extend(eval(self.__tableName__+".objects.filter(Day__exact=self.__startDay__).filter(Time__gte=self.__startTime__).filter(Time__lte=self.__endTime__)"))
		else:
			self.__querylist__.extend(eval(self.__tableName__+".objects.filter(Day__gt=self.__startDay__).filter(Day__lt=self.__endDay__)"))
			self.__querylist__.extend(eval(self.__tableName__+".objects.filter(Day__exact=self.__startDay__).filter(Time__gte=self.__startTime__)"))
			self.__querylist__.extend(eval(self.__tableName__+".objects.filter(Day__exact=self.__endDay__).filter(Time__lte=self.__endTime__)"))
		
	def query_list(self):
		"""
		this function store the related info into returnQueryList, which is as below:
		if connterList = [counter1,counter2,counter3]
		the returnQueryList =
		[
			[timeStamp1, counter1value,counter2value,counter3value],
		 	......
		]
		"""
		self.query()
		for record in self.__querylist__:
			temp_list = []
			timeStamp = str(record.Day) + " " + str(record.Time)
			temp_list.append(timeStamp)
			for counter in self.__counterList__:
				temp_list.append(eval("record."+counter))
			self.returnQueryList.append(temp_list)
			  
		return self.returnQueryList

	

