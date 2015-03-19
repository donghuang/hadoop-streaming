#!/usr/bin/env bash

ETL_DATE=20140101
SCRIPT=`basename $0`

hadoop fs -test -d $ETL_DATE 2>&1 2>/dev/null
[ $? -eq 0 ] || hadoop fs -mkdir $ETL_DATE

hadoop fs -test -d $ETL_DATE/$SCRIPT 2>&1 2>/dev/null
[ $? -eq 0 ] && hadoop fs -rmr $ETL_DATE/$SCRIPT 

hadoop jar /home/hadoop/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar \
-jobconf mapred.map.max.attempts=1 \
-jobconf mapred.reduce.max.attempts=1 \
-input /test/aaa \
-output $ETL_DATE/$SCRIPT \
-cmdenv etldate=$ETL_DATE \
-mapper  mapper.sh \
-reducer reducer.sh \
-file mapper.sh \
-file reducer.sh 

#-D mapred.job.name="xxx" \
#-D mapred.map.tasks=3 \
#-D mapred.reduce.tasks=2 \
#-jobconf mapred.map.max.attempts=1 \  每个map task最大尝试次数
#-jobconf mapred.reduce.max.attempts=1 \ 每个reduce task最大尝试次数