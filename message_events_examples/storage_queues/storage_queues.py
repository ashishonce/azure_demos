import os 
import time
import random
import base64
from azure.storage.queue import (QueueService, QueueMessageFormat)
import config

#simple example for how to create a Queue service and post a message in azure storage queue.
#We already have a pre configured Queue in azure with name "myqueue-items"
queue_service = QueueService(account_name=config.storageAccountName, account_key=config.storageAccountKey)

queue_service.encode_function = QueueMessageFormat.text_base64encode;

def run_queue():
    message = u'this is from the python tutorial';
    queue_service.put_message('myqueue-items', message);

if 1:
    run_queue();
    



