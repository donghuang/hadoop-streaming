#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

count=0
started=0
country=""
persontype=""
#reducer函数接收的是 标准输入的数据
for line in sys.stdin:
	if line.strip()=="":
		continue

	fields=line[:-1].split("\t")
	newcountry=fields[0]
	newpersontype=fields[1]

	if newcountry!=country or newpersontype!=persontype:
		if started!=0:
			print country,"\t",persontype,"\t",count
		country=fields[0]
		persontype=fields[1]
		started=1
		count=1
	else:
		count=count+1

print country,"\t",persontype,"\t",count