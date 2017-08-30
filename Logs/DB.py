import logging
import json


def exm1():
    d = {'name':'Alex',
         'age':42,
         'address':{'city':'Odessa', 'street':"Deribasovskaya"},
         'data':[[[1,'2',True]]]}

    jsoned = json.dumps(d)
    print(jsoned)

    with open("C:\Users\k.belous\Desktop\\test_json.txt", 'w') as f:
        f.write(jsoned)

    with open("C:\Users\k.belous\Desktop\\test_json.txt", 'r') as f:
        content = f.read()

    obj = json.loads(content)
    f =
    print(type(obj), obj)
    print f


def exp2():

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('test.log')
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s'))
    logger.addHandler(handler)

    d = {'name':'Alex',
         'age':42,
         'address':{'city':'Odessa', 'street':"Deribasovskaya"},
         'data':[[[1,'2',True]]]}

    jsoned = json.dumps(d)
    print(jsoned)

    prefix = "Dumped: "
    logger.info("%s %s", prefix, jsoned)
    logging.shutdown()

    with open('test.log', 'r') as f:
        last_line = f.readlines()[-1]
        restored = last_line.split(prefix)[1]

    obj = json.loads(restored)
    print(type(obj), obj)


if __name__ == '__main__':
    exm1()
    #exm2()