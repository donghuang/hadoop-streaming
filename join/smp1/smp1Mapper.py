#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


for line in sys.stdin:
	personName = "-1" #default sorted as first
	personType = "-1" #default sorted as first
	countryName = "-1" #default sorted as first
	country2Digit = "-1" #default sorted as first
	if line.strip()=="":
		continue
	#line的最后为"\n"，需要剔除
	fields=line[:-1].split("|") 
	if len(fields)==2: #country data
		countryName=fields[0]
		country2Digit=fields[1]
	else: #customer data
		personName=fields[0]
		personType=fields[1]
		country2Digit=fields[2]
	
	print '%s\t%s\t%s\t%s' % (country2Digit,personType,personName,countryName)
