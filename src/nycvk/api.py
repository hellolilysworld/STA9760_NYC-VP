#import pandas as pd

from sodapy import Socrata

def get_data(app_key,page_size,num_pages):

		
	client = Socrata("data.cityofnewyork.us",app_key)

	#pag = page_size * (num_pages - 1)
	results = []
	for i in range(0, num_pages):
		results.append(client.get('nc67-uf89', limit=page_size, offset=i*(page_size)))
		
	# results = client.get("nc67-uf89", limit=page_size, offset = pag) #get results.json
	#results_df = pd.DataFrame.from_records(results)
	return results
	# print(results)