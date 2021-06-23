from django.db import models

class Student(models.Model):
	nameOfTheBoard = models.CharField(max_length=255,unique=True)
	No_Boys_Appeared = models.IntegerField(default=0)
	No_Girls_Appeared = models.IntegerField(default=0)
	Total_Appeared = models.IntegerField(default=0)
	No_Boys_Passed  = models.IntegerField(default=0)
	No_Girls_Passed  = models.IntegerField(default=0)
	No_Total_Passed  = models.IntegerField(default=0)
	SC_No_Boys_Appeared  = models.IntegerField(default=0)
	SC_No_Girls_Appeared  = models.IntegerField(default=0)
	SC_No_Total_Appeared  = models.IntegerField(default=0)
	SC_No_Boys_Passed  = models.IntegerField(default=0)
	SC_No_Girls_Passed  = models.IntegerField(default=0)
	SC_No_Total_Passed  = models.IntegerField(default=0)
	ST_No_Boys_Appeared  = models.IntegerField(default=0)
	ST_No_Girls_Appeared  = models.IntegerField(default=0)
	ST_No_Total_Appeared  = models.IntegerField(default=0)
	ST_No_Boys_Passed  = models.IntegerField(default=0)
	ST_No_Girls_Passed  = models.IntegerField(default=0)
	ST_No_Total_Passed  = models.IntegerField(default=0)
	current_timeStamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.nameOfTheBoard