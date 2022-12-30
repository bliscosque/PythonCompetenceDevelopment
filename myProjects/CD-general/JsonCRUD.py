import json

def get_json_data():
    try:
        with open("example.json") as dFile:
            data=json.load(dFile)
        return data
    except FileNotFoundError:
        with open("example.json","w") as dFile:
            dFile.write("")  
            return {}

def store_json_data(data):
    with open("example.json","w") as dFile:
            json.dump(data,dFile)  

# CREATE
def add_usr(name,passwd):
    dct={
        "name":name,
        "pass":passwd
    }
    data=get_json_data()
    data[name]=dct # a chave também é o nome
    store_json_data(data)

# READ ALL
def get_all_usr():
    data=get_json_data()
    return data

# READ ONE (pelo nome, que é a chave)
def get_usr(name):
    data=get_json_data()
    if name in data:
        return data[name]
    return None

# UPDATE
def update_usr(name, passwd):
    data=get_json_data()
    if name in data:
        dct={
            "name":name,
            "pass":passwd
        }
        data=get_json_data()
        data[name]=dct # a chave também é o nome
        store_json_data(data)
        return "OK"
    return "NOK"

# DELETE
def delete_usr(name):
    data=get_json_data()
    if name in data:
        data.pop(name)
        store_json_data(data)
        return "OK"
    return "NOK"

add_usr('thiago','123')
add_usr('thiago2','345')
print(get_all_usr())
print(get_usr('thiago'))
print(get_usr('NAO'))
print(update_usr('thiago','987'))
print(update_usr('NAO','987'))
print(get_all_usr())
print(delete_usr('thiago2'))
print(delete_usr('NAO'))
print(get_all_usr())