#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

#打开分发到各节点的数据文件
filepath = os.environ["mapred_cache_files"]
filename = filepath.split('#')
f=open(filename[1],'r')

#mapper函数接收的是 标准输入的数据
for line in sys.stdin:
	if line.strip()=="":
		continue
	
	fields=line[:-1].split("|")
	flg=0
	for joinline in f:
		if joinline.strip()=="":
			continue

		joinfields=joinline[:-1].split("|")
		if fields[2]==joinfields[1]:
			print joinfields[0],"\t",fields[1],"\t",1
			flg=1
			continue
	if flg==0:
		print "Unknown Country","\t",fields[1],"\t",1
		
	#移动到数据文件开始位置
	f.seek(0,0)

f.close()
