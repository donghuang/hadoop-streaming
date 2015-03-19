# -*- coding: utf-8 -*-
#reducer.py

import sys

def reducer():
	#为了记录和上一个记录的区别，用lastsno记录上个sno
	lastsno = ""

	for line in sys.stdin:
		if line.strip()=="":
			continue
		fields = line[:-1].split("\t")
		sno = fields[0]
		'''
		处理思路：
		遇见当前key与上一条key不同并且label=0，就记录下来name值，
		当前key与上一条key相同并且label==1，则将本条数据的courseno、
		grade联通上一条记录的name一起输出成最终结果
		'''
		if sno != lastsno:
			name=""
			#这里没有判断label==1的情况，
			#因为sno!=lastno,并且label=1表示该条key没有数据源1的数据
			if fields[1]=="0":
				name=fields[2]
				
		elif sno==lastsno:
			#这里没有判断label==0的情况，
			#因为sno==lastno并且label==0表示该条key没有数据源2的数据
			
			if fields[1]=="1":
				courseno=fields[2]
				grade=fields[3]
				
				if name:
					print '\t'.join((lastsno,name,courseno,grade))
		lastsno = sno

if __name__=='__main__':
	reducer()