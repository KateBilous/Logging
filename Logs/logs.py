import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler('JsonLog.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s'))
ch.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s'))
logger.addHandler(fh)
logger.addHandler(ch)

dict_atributes = {
    'job_lunch_id': 4, 'job_id': 7, 'application_lunch_id': '', ' application_id': '', ' time': "",
    'status': "", 'output': "", 'other_notes': ""}

dumped_data = json.dumps(dict_atributes)
print(type(dumped_data))

prefix = "Inserted: "
logger.info("%s %s", prefix, dumped_data)
logging.shutdown()

with open('JsonLog.log', 'r') as f:
    last_line = f.readlines()[-1]
    restored = last_line.split(prefix)[1]
    print restored

obj = json.loads(restored)
print (type(obj), obj)


def parsJson():
    obj = json.loads(restored)
    print (type(obj), "kijdfiuedhegui", obj)

    for key, value in obj.iteritems():
        print  value


call = parsJson()
