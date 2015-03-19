#!/usr/bin/env bash

ETL_DATE=20150301
OUTPUT="$ETL_DATE/`basename $0`"

hadoop fs -test -d $ETL_DATE 2>&1 2>/dev/null
[ $? -eq 0 ] || hadoop fs -mkdir $ETL_DATE

hadoop fs -test -d $ETL_DATE/$SCRIPT 2>&1 2>/dev/null
[ $? -eq 0 ] && hadoop fs -rmr $OUTPUT

hadoop jar /home/hadoop/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar \
-jobconf mapred.job.name="map side join" \
-jobconf stream.num.map.output.key.fields=2 \
-input /test/customers.dat \
-output $OUTPUT \
-mapper "python mapper.py" \
-reducer "python reducer.py" \
-file mapper.py \
-file reducer.py \
-cacheFile hdfs://master:9000/user/countries.dat#link_countries 


#三种文件分发方式的区别：
#-file 将客户端本地文件打成jar包上传到HDFS然后分发到计算节点，
#-cacheFile 将HDFS文件分发到计算节点，
#-cacheArchive 将HDFS压缩文件分发到计算节点并解压。

#指定在第二个分隔符处进行分隔，也就是第二个分隔符之前的作为key，之后的作为value。streaming 会按照key自动排序
#-jobconf stream.num.map.output.key.fields=2 

[ $? -eq 0 ] && echo "返回[$?]:执行成功" || echo "返回[$?]:执行失败"