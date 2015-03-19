#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


lastcountry2Digit=""
lastcountryName=""
lastpersonType=""
count=0
for line in sys.stdin:
	if line.strip()=="":
		continue
	fields=line[:-1].split("\t")
	
	if fields[0]!=lastcountry2Digit:
		lastcountry2Digit=fields[0]
		lastcountryName=fields[3]
		flg=0
	else:
		if flg==0:
			lastpersonType=fields[1]
			count=1
		if lastpersonType!=fields[1]:
			print lastcountryName,lastpersonType,count
			flg=flg+1
		else:
			count=count+1
			flg=flg+1
		  
			
			
	
	
	