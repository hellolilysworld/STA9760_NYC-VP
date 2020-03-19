import argparse
from src.api import get_data
from time import sleep

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--page_size", type=int)
    parser.add_argument("--num_pages", default=None, type=int)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    
    j = 0
    while True:
    	j += 1

    	get_data(args.page_size, args.num_pages, args.output, j)

    	print(f"DONE LOADING {j}, SLEEPING...")
    	sleep(3)


    



    
