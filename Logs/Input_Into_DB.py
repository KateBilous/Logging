import json
from logs import formatLogin




def input_into_db():
    pass

def pars_json():

    parsed_json = json.load(formatLogin.json_list)
    print(type(parsed_json))
    # job_lunch_id =(pars_json([job_lunch_id]))
    # job_id =
    # application_lunch_id =
    # application_id =
    # time =
    # status =
    # output =
    # other_notes =
    # result = map (lambda x:x['value'],pars_json())
    # print(result)
    # results = [item['value'] for item in pars_json()]
    # print results
    for key, value in parsed_json.split(":"):
        print key, value

call = pars_json()
print(call)