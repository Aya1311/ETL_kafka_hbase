from kafka import KafkaConsumer
from json import loads
from rich import print
import pydoop.hdfs as hdfs
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import happybase
# HBase configuration
hbase_host = 'localhost'
hbase_port = 9090
hbase_table_name = 'table_aya'
# Create a Kafka consumer
consumer = KafkaConsumer(
    'topic_aya',  # Topic to consume messages from
    bootstrap_servers=['localhost:9092'],  # Kafka server addresses
    auto_offset_reset='earliest',  # Reset offset to the earliest available message
    enable_auto_commit=True,  # Enable auto commit of consumed messages
    group_id=None,  # Consumer group ID (None indicates an individual consumer)
)
#opptional
# hdfs_path = 'hdfs://localhost:9000/kafka_demo/tweets_data.json'  # Path to the HDFS file


# Connect to HBase
transport = TTransport.TBufferedTransport(TSocket.TSocket(hbase_host, hbase_port))
transport.open()
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = happybase.Connection(host=hbase_host, port=hbase_port).table(hbase_table_name)

# Process incoming messages
for message in consumer:
    tweet = message.value  # Get the value of the message (tweet)
    print(tweet)  # Print the tweet
    print("Storing in HBase!")
    client.put(b'row_key', {b'cf1:data': tweet.decode('utf-8')})


  # with hdfs.open(hdfs_path, 'at') as file:
       # print("Storing in HDFS!")
     #   file.write("{}\n".format(tweet))
