import logging
import json

logging.basicConfig(filename='logs_in_json.log', level=logging.DEBUG, format='%(filename)s:%(levelno)s:%(asctime)s:'
                                                                             '%(process)d:%(processName)s:%(message)s:')
class formatLogin:



    json_list = []
    json_list.append(
    {"job_lunch_id": 4 , "job_id": 7, "application_lunch_id": '', " application_id":'' , " time": "",
     "status": "", "output": "", "other_notes": ""})



    #log_file = logging.info(json_list)
    #print(type(log_file))
