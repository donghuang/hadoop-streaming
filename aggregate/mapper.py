#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os

for line in sys.stdin:
	if line.strip()=="":
		continue
	fields=line[:-1].split("\t")
	print "LongValueSum:%s %s\t1" % (fields[0],fields[1])
	#print "LongValueSum:",'b',
	#print "ValueHistogram:",fields[0],"\t",fields[1]
	