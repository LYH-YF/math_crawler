from pymongo import MongoClient
from config import *

id_list=[['phone1','pwd1'],['phone2','pwd2'],['phone3','pwd3']]

#create collection for our ID and password
def create_id_database():
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        db=client['IDdata']
        collection=db['ID']

#a function to insert id and password to collection of mongodb
def insert_id(id_dict):
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        collection=client.IDdata.ID
        collection.insert(id_dict)

#from mongodb get id and password datas
def get_id():
    id_list=[]
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        collection=client.IDdata.ID
        for i in list(collection.find()):
            id_list.append({'phone':i['phone'],'password':i['password']})
    return id_list

if __name__ == "__main__":
    client=create_id_database()
    
    for i in id_list:
        id_dict={'phone':i[0],'password':i[1]}
        #print(id_dict)
        insert_id(id_dict)
    #print('insert finish')
    
    id_list=get_id()
