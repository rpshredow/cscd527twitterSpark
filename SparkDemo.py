# SparkDemo.py
# This code is copyright (c) 2017 by Laurent Weichberger.
# Authors: Laurent Weichberger, from Hortonworks and,
# from RAND Corp: James Liu, Russell Hanson, Scot Hickey,
# Angel Martinez, Asa Wilks, & Sascha Ishikawa
# This script does use Apache Spark. Enjoy...
# This code was designed to be run as: spark-submit SparkDemo.py
 
import time
import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
 
# Our filter function:
def filter_tweets(tweet):
    json_tweet = json.loads(tweet)
    if json_tweet['text'].startswith('RT') or json_tweet['text'].startswith('@'):
        return False # filter() requires a Boolean value
    return True
 
sc = SparkContext("local[*]", "Twitter Demo")
ssc = StreamingContext(sc, 10) #10 is the batch interval in seconds
IP = "localhost"
Port = 5556
lines = ssc.socketTextStream(IP, Port)

lines.foreachRDD( lambda rdd: rdd.filter( filter_tweets ).coalesce(1).saveAsTextFile("./tweets/%f" % time.time()) )
ssc.start()
ssc.awaitTermination()