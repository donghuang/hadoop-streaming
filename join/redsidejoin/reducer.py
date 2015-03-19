#!/usr/bin/env python
# -*- coding: utf-8 -*-
#reducer.py

import sys

def reducer():
	#为了记录和上一个记录的区别，用last_country2digit记录上个country2digit
	last_country2digit = ""

	for line in sys.stdin:
		if line.strip()=="":
			continue
		fields = line[:-1].split("\t")
		country2digit = fields[0]
		'''
		处理思路：
		遇见当前key与上一条key不同并且label=0，就记录下来country值
		当前key与上一条key不同并且label==1，说明本条数据无country值,直接输出
		当前key与上一条key相同并且label==1，则将本条数据的person、persontype和上一条记录的country一起输出成最终结果
		'''
		if country2digit != last_country2digit:
			country=""
			if fields[1]=="0":
				country=fields[2]
			if fields[1]=="1":
				country="Unknown Country"
				print '\t'.join((country,fields[2],fields[3]))
				
		elif country2digit==last_country2digit:
			if fields[1]=="1":
				person=fields[2]
				persontype=fields[3]
				
				if country:
					print '\t'.join((country,person,persontype))
		last_country2digit = country2digit

if __name__=='__main__':
	reducer()