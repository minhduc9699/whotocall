import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds147469.mlab.com:47469/who-2-call

host = "ds147469.mlab.com"
port = 47469
db_name = "who-2-call"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
