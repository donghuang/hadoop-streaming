#!/usr/bin/env bash

ETL_DATE=20140101
SCRIPT=`basename $0`

hadoop fs -test -d $ETL_DATE 2>&1 2>/dev/null
[ $? -eq 0 ] || hadoop fs -mkdir $ETL_DATE

hadoop fs -test -d $ETL_DATE/$SCRIPT 2>&1 2>/dev/null
[ $? -eq 0 ] && hadoop fs -rmr $ETL_DATE/$SCRIPT 

hadoop jar /home/hadoop/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar \
-jobconf mapred.job.name="join--sno_name-sno_courseno_grade" \
-jobconf stream.num.map.output.key.fields=2 \
-input /test/student* \
-output $ETL_DATE/$SCRIPT \
-mapper 'python mapper.py' \
-reducer 'python reducer.py' \
-file mapper.py \
-file reducer.py 



#-jobconf mapred.map.tasks=10 \
#-jobconf mapred.reduce.tasks=5 \
#-jobconf mapred.job.map.capacity=10 \
#-jobconf mapred.job.reduce.capacity=5 \
#二次排序
#-jobconf map.output.key.field.separator=. \ #改变map输出中key和value的分隔符
#-jobconf stream.num.map.output.key.fields=2 \ #指定在第二个分隔符处进行分隔，也就是第二个分隔符之前的作为key，之后的作为value。
#-jobconf num.key.fields.for.partition=2 \ #指定将key分隔出来的前两个部分而不是整个key用于Partitioner做partition
#-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \

#三种文件分发方式的区别：-file将客户端本地文件打成jar包上传到HDFS然后分发到计算节点，-cacheFile将HDFS文件分发到计算节点，-cacheArchive将HDFS压缩文件分发到计算节点并解压。
#-cacheArchive "/share/python26.tar.gz#python26"

echo $?
