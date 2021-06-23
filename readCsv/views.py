from django.shortcuts import render,get_object_or_404 
from .models import Student

import csv

def home(request):
	filename = './static/SES_2007-08_TABLE29.csv'
	with open(filename,'r') as f:
		reader = csv.reader(f)
		flag=0
		for i, row in enumerate(reader):
			if i==0:
				pass
			else:
				# Students = Student.objects 
				# for Student1 in Students:
				#  	if Student1.nameOfTheBoard!=row[0]:
				#  		flag=1
				# if flag==1:
				try:
					Student.objects.create(
					nameOfTheBoard = row[0],
					No_Boys_Appeared = row[1],
					No_Girls_Appeared = row[2],
					Total_Appeared = row[3],
					No_Boys_Passed = row[4],
					No_Girls_Passed = row[5],
					No_Total_Passed = row[6],
					SC_No_Boys_Appeared  = row[7],
					SC_No_Girls_Appeared  = row[8],
					SC_No_Total_Appeared  = row[9],
					SC_No_Boys_Passed  = row[10],
					SC_No_Girls_Passed  = row[11],
					SC_No_Total_Passed   = row[12],
					ST_No_Boys_Appeared  = row[13],
					ST_No_Girls_Appeared  = row[14],
					ST_No_Total_Appeared  = row[15],
					ST_No_Boys_Passed  = row[16],
					ST_No_Girls_Passed  = row[17],
					ST_No_Total_Passed   = row[18]
					)
				except:
					pass
	Students = Student.objects
	return	render(request, 'csvs/index.html',{'Students':Students})
