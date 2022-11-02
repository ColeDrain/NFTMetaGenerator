import json, csv, os, hashlib
import pandas as pd


n_format = "CHIP-0007"
collection_name = "Zuri NFT Tickets for Free Lunch"
collection_description = "Zuri NFT Tickets for Free Lunch"
collection_id = "b774f676-c1d5-422e-beed-00ef5510c64d"
csv_path = 'csv\main.csv'


def hash_jsons(filename):
    '''Generates SHA256 for a file'''
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
    return readable_hash


def generate_final_output(hash_list):
    '''Appends Hashes to Original CSV'''
    df = pd.read_csv('csv\main.csv')
    df['Hash'] = hash_list
    df.to_csv('output/final_output.csv', index=False)


def main(filepath):
    '''Calls other functions'''

    hash_list = []
    jsondata = {}
    collection = {}

    collection['name'] = collection_name
    collection['id'] = collection_id


    with open(filepath,'r') as csvfile:
        csvreader = list(csv.reader(csvfile))
        for i in range(1, len(csvreader)):
            attributes_list = []

            series_number = csvreader[i][0]
            name = csvreader[i][1]
            sensitive_content = False
            description = csvreader[i][3]
            gender = csvreader[i][4]
            series_total = 562

            attributes_list.append({"trait_type":"Gender","value":gender})

            jsondata['format'] = n_format
            jsondata['name'] = name
            jsondata['description'] = description
            jsondata['series_number'] = series_number
            jsondata['series_total'] = series_total
            jsondata['sensitive_content'] = sensitive_content

            jsondata['attributes'] = attributes_list
            jsondata['collection'] = collection


            with open(f"metadata/{name}.json","w") as f:
                f.write(json.dumps(jsondata, indent=4))

            hash_list.append(hash_jsons(f"metadata/{name}.json"))

        generate_final_output(hash_list)



if __name__ == "__main__":
    main_function(csv_path)


# filename.output.csv