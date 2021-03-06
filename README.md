# NYC Parking Violations

## Part1	

### Installing in `requirements.txt`

```
certifi==2019.11.28
chardet==3.0.4
idna==2.9
requests==2.23.0
urllib3==1.25.8
pandas==0.24.1
sodapy==1.5.0
```

### Python Scripts

##### Get the data from API using `sodapy`
`nycvpp/src/nycvpk/api.py`

```
from sodapy import Socrata

def get_data(app_key,page_size,num_pages):
	
	client = Socrata("data.cityofnewyork.us",app_key)

	results = []
	for i in range(0, num_pages):
  ```
  ##### in sodapy each the total amount of data = limit * number of pages, offset=the start of each new page
  ```
		results.append(client.get('nc67-uf89', limit=page_size, offset=i*(page_size)))
	return results
  ```

#### Call the function in `main.py`

```

import os

import argparse

```
##### The `OS` module in python provides functions for interacting with the operating system. 
##### The `argparse` module makes it easy to write user-friendly command-line interfaces. It parses the defined arguments from the sys. argv .

```
from src.nycvk.api import get_data

if __name__ == "__main__":

	app_key = os.getenv(f'APP_KEY')
	print(app_key)
	parser = argparse.ArgumentParser()
	parser.add_argument("--page_size", type=int)
	parser.add_argument("--num_pages", default=None, type=int)
	parser.add_argument("--output", default=None)
	args = parser.parse_args()
    
	data=get_data(app_key, args.page_size, args.num_pages)
	with open(args.output, "w") as outfile: 	

		for lines in data:
			for line in lines:
				outfile.write(f"{line}"+'\n')
```


  
#### Commands
`docker run -v $(pwd):/app -e APP_KEY={YOUR_APP_KEY} -t bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json`

## Part2
#### Commands
 
 `docker-compose run -e APP_KEY={YOUR_APP_KEY} -v ${PWD}:/app pyth python -m main --page_size=100 --num_pages=20 —output=results.json`
 
#### Query ElasticSearch
##### query 1 record of New Jersey and the license_type:PAS, output is save as `output.txt` in part2.

 `curl -o output.txt http://localhost:9200/nycvp/violations/_search\?q\=state:NJ+license_type:PAS&size=1`
 
##### results can also be found in 
  
  http://localhost:9200/nycvp/violations/_search?q=state:NJ+license_type:PAS&size=1
  
  

## Part3
### Average penalty_Amount VS average fine amount over five years
![](/part3/1.png)

### Average reduction amount by county
![](/part3/2.png)

### Most popular violation
![](/part3/3.png)

### payment_amount range distribution 
![](/part3/4.png)






