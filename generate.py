import json, csv, os
from pathlib import Path
from metadata_config import *

csvs_path = 'csvs/'

def main_function(filepath):
    jsondata = {}

    collection = {}
    collection['name'] = collection_name
    collection['id'] = collection_uuid

    n_format = "CHIP-0007"

    with open(filepath,'r') as csvfile:
        csvreader = list(csv.reader(csvfile))
        for i in range(len(csvreader)):
            attributes_list = []
            if i == 0:
                if indvdl_attributes == True:
                    attribute_names = csvreader[0][4:]
                    num_attributes=len(attribute_names)
                    print (f"Detected {num_attributes} attributes")
            else:
                series_number = csvreader[i][0]
                name = csvreader[i][1]
                sensitive_content = False
                description = f'description for {name}'
                series_total = 400
                if indvdl_attributes == True:
                    for j in range(num_attributes):
                        k = j + 4
                        attributes_list.append({"trait_type":attribute_names[j],"value":csvreader[i][k]})
                jsondata['format'] = n_format
                jsondata['name'] = name
                jsondata['description'] = description
                jsondata['series_number'] = series_number
                jsondata['series_total'] = series_total
                jsondata['sensitive_content'] = sensitive_content
                if indvdl_attributes == True:
                    jsondata['attributes'] = attributes_list
                jsondata['collection'] = collection


                with open(f"metadata/{name}.json","w") as f:
                    f.write(json.dumps(jsondata, indent=4))
    print("Metadata generation complete! You can find it in the /metadata folder. Thanks for using this tool.")

if __name__ == "__main__":
    # iterate over files in
    # csvs directory
    for filename in os.listdir(csvs_path):
        f = os.path.join(csvs_path, filename)
        main_function(f)


filename.output.csv