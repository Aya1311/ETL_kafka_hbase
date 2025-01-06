# Import necessary libraries
from kafka import KafkaConsumer
from json import loads
from rich import print
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
    auto_offset_reset='latest',  # Reset offset to the latest available message
    enable_auto_commit=True,  # Enable auto commit of consumed messages
    group_id=None,  # Consumer group ID (None indicates an individual consumer)
   
)

connection = happybase.Connection(hbase_host, hbase_port)
table = connection.table(hbase_table_name)
# Connect to HBase
#transport = TTransport.TBufferedTransport(TSocket.TSocket(hbase_host, hbase_port))
#transport.open()
#protocol = TBinaryProtocol.TBinaryProtocol(transport)
#client = Hbase.Client(protocol)

# Process incoming messages
for message in consumer:
    tweet = message.value  # Get the value of the message (tweet)
    print(tweet)  # Print the tweet
    
   # Store in HBase
table.put('row_key', {'cf1:data': tweet})
# Store in HBase
#mutations = [Hbase.Mutation(column='cf1:data', value=tweet)]
#client.mutateRow(hbase_table_name, 'row_key', mutations)
