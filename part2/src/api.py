from datetime import datetime
from elasticsearch import Elasticsearch
from sodapy import Socrata
from requests import get
from time import sleep
import json
import os

app_key = os.getenv('APP_KEY')
client = Socrata("data.cityofnewyork.us",app_key)

def create_and_update_index(index_name):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except:
        pass
    return es

def push(result, es, index, doc_type):
    for key, value in result.items():
        if '_amount' in key:
            result[key] = float(value)
        elif '_date' in key:
            result[key] = datetime.strptime(value, '%m/%d/%Y').date()
    res = es.index(index=index, doc_type=doc_type, body=result)
    print(res['result'], result['summons_number'], 'successfully')

def get_data(page_size, num_pages, output, round):
    es = create_and_update_index('nycvp')
    for i in range(0+round, num_pages+round):
        results = client.get('nc67-uf89', limit=page_size, offset=i*(page_size))
        for result in results:
            with open(output, 'a') as temp: 
                temp.write(json.dumps(result) + '\n')
            push(result, es, 'nycvp', 'violations')
