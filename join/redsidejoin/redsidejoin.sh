#!/usr/bin/env bash

ETL_DATE=20150301
OUTPUT="$ETL_DATE/`basename $0`"

hadoop fs -test -d $ETL_DATE 2>&1 2>/dev/null
[ $? -eq 0 ] || hadoop fs -mkdir $ETL_DATE

hadoop fs -test -d $ETL_DATE/$SCRIPT 2>&1 2>/dev/null
[ $? -eq 0 ] && hadoop fs -rmr $OUTPUT

hadoop jar /home/hadoop/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar \
-jobconf mapred.job.name="reduce side join" \
-jobconf stream.num.map.output.key.fields=2 \
-input /test/countries.dat \
-input /test/customers.dat \
-output $OUTPUT \
-mapper 'python mapper.py' \
-reducer 'python reducer.py' \
-file mapper.py \
-file reducer.py 

[ $? -eq 0 ] && echo "返回[$?]:执行成功" || echo "返回[$?]:执行失败"
