import sys
import json
import string
from time import time
import logging

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext, DStream

from settings import \
    EMAIL_DESTINATION, \
    NOTIFICATION_MESSAGE, \
    SOCKET_HOST, \
    SOCKET_PORT, \
    WATER_LEVEL_THRESHOLD

from sendmail import send_email

logging.basicConfig(filename="logger_spark.log", level=logging.DEBUG)


def send_mail(rdd, acc1, acc2):
    rdd.foreach(lambda _: acc1.add(1))
    print("COUNTER BELOW THRESHOLD : " + str(acc1.value))
    if (acc1.value % 10 == 0 and acc1.value != 0 and acc2.value == 0):
        acc2.add(1)
        print("SENDING EMAIL")
        send_email(EMAIL_DESTINATION, NOTIFICATION_MESSAGE)
    elif (acc1.value % 10 != 0 and acc2.value == 1):
        if(acc2.value > 0):
            acc2.add(-1)


conf = SparkConf().setAppName(
    "Arduino Notification").setMaster('local[*]')

sparkContext = SparkContext(conf=conf)
sparkContext.setLogLevel("ERROR")

streamingContext = StreamingContext(sparkContext, 1)

dstream = streamingContext.socketTextStream(SOCKET_HOST, SOCKET_PORT)
# Micro Batches

# Sensor stream
count_sensor_read = sparkContext.accumulator(0)
status_mailed = sparkContext.accumulator(0)

data = dstream.filter(lambda _data: float(_data) <= WATER_LEVEL_THRESHOLD)

data.foreachRDD(lambda rdd: send_mail(rdd, count_sensor_read, status_mailed))

data.pprint()
# End of sensor stream
# End of micro batches

streamingContext.start()
streamingContext.awaitTermination()
