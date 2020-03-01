# NYC Parking Violations

## Part 1: Python Scripting	

### File Structure
  ```console
  $ tree
  ```

  ```console
  .
  ├── Dockerfile
  ├── main.py
  ├── requirements.txt
  └── src
      └── bigdata1
          └── api.py

  2 directories, 4 files
  ```

### Packages 
- Specified in `requirements.txt`

  - `requests`
  - `pandas`
  - `numpy`
  - `sklearn`
  - `pytest`
  - `pyyaml`
  - `matplotlib`
  - `pygithub`
  - `scipy`
  - `sodapy`
  - `pprint`
  
### Python Scripts

- `main.py`

```py
import argparse

from src.bigdata1.api import get_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--page_size", type=int)
    parser.add_argument("--num_pages", default=None, type=int)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    get_results(args.page_size, args.num_pages, args.output)
 ```

- `src/bigdata1/api.py`

```py
import os
import json 
import pprint
from sodapy import Socrata

data_id = 'nc67-uf89'
client = Socrata('data.cityofnewyork.us', os.environ.get("APP_KEY"))
count = int(client.get(data_id, select='COUNT(*)')[0]['COUNT'])

def get_results(page_size, num_pages, output):
    if not num_pages:
        num_pages = count // page_size + 1
    if output:
        create_records(output)
    for page in range(num_pages):
        offset = page * page_size
        page_records = client.get(data_id, limit=page_size, offset=offset)
        for record in page_records:
            if output:
                add_record(record, output)
            else:
                pprint.pprint(record, indent=4)

def create_records(output):
    with open(output, 'w') as out_file:
        pass

def add_record(record, output):
    with open(output, 'a') as out_file: 
        out_file.write(json.dumps(record) + '\n')
```

  
#### Commands
`docker run -v $(pwd):/app -e APP_KEY=`{YOUR_APP_KEY}` -t bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results3.json 


