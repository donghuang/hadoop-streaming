# -*- coding: utf-8 -*-
#Mapper.py

import os
import sys

def mapper():
	#获取当前正在处理的文件的名字，这里我们有两个输入文件
	filepath = os.environ["map_input_file"]
	filename = os.path.split(filepath)[-1]
	for line in sys.stdin:
		if line.strip()=="":
			continue
		fields = line[:-1].split("|")
		
		#以下判断filename的目的是不同的文件有不同的字段，并且需加上不同的标记
		if filename == 'countries.dat':
			country = fields[0]
			country2digit = fields[1]
			#下面的数字'0'就是为countries.da加上的统一标记
			print '\t'.join((country2digit,'0',country))
		elif filename == 'customers.dat':
			person = fields[0]
			persontype  = fields[1]
			country2digit = fields[2]
			#下面的数字'1'就是为customers.dat加上的统一标记
			print '\t'.join((country2digit,'1',person,persontype))

if __name__=='__main__':
	mapper()
