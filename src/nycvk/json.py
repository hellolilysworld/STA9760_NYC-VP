import json

def save_as_json(data,output):
	#json_object = json.dumps(data, indent=4)
	#json_object = json.dumps(data)
	#json_object = to_json(data)
	with open(output, "w") as outfile: 
		outfile.write(f"{data}")

