import logging 
import azure.functions as func   
import json
from typing import List
def main(events: List[func.EventHubEvent],outputDocument: func.Out[func.Document]):   
     for event in events:
            
            event_data = event.get_body()
            logging.info(event_data)
            my_json = event_data.decode('utf8').replace("'", '"')
            outputDocument.set(func.Document.from_json(my_json))
            logging.info(my_json)