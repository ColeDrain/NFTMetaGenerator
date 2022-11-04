import json, csv, os, hashlib
import pandas as pd

# Constants
n_format = "CHIP-0007"
collection_name = "Zuri NFT Tickets for Free Lunch"
collection_description = "Zuri NFT Tickets for Free Lunch"
collection_id = "b774f676-c1d5-422e-beed-00ef5510c64d"

csv_path = 'csv/main.csv'


def hash_jsons(filename):
    '''Generates SHA256 for a file'''
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
    return readable_hash


def generate_final_output(hash_list):
    '''Appends Hashes to Original CSV'''
    df = pd.read_csv('csv\main.csv')
    df['Hash'] = hash_list
    df.to_csv('output/final.output.csv', index=False)


def func_main(filepath):
    '''Calls other functions'''

    hash_list = []
    jsondata = {}
    collection = {}

    collection['name'] = collection_name
    collection['id'] = collection_id
    collection_attributes = {
            "type": collection_description,
            "value": "Rewards for accomplishments during HNGi9."
    }
    collection['attributes'] = [collection_attributes]

    with open(filepath,'r') as csvfile:
        csvreader = list(csv.reader(csvfile))
        for i in range(1, len(csvreader)):

            attributes_list = []

            # Get nft values
            minting_tool = csvreader[i][0]
            series_number = int(csvreader[i][1])
            name = csvreader[i][2]
            sensitive_content = False
            description = csvreader[i][4]
            gender = csvreader[i][5]
            attributes_list.append({"trait_type":"gender","value":gender})
            attributes = csvreader[i][6]
            series_total = 420
            attributes = attributes.split(";")
            if attributes[-1] == '':
                attributes.remove('')
            try:
                for attr in attributes:
                    attr_map = attr.split(":")
                    attr_name = attr_map[0].strip()
                    attr_value = attr_map[1].strip()
                    if attr_value.lower() != 'none':
                        attributes_list.append({"trait_type":attr_name,"value":attr_value})
            except:
                print("This row has issues:")
                print(csvreader[i])

            jsondata['format'] = n_format
            jsondata['name'] = name
            jsondata['description'] = description
            jsondata['minting_tool'] = minting_tool or ''
            jsondata['series_number'] = series_number
            jsondata['series_total'] = series_total
            jsondata['sensitive_content'] = sensitive_content

            jsondata['attributes'] = attributes_list
            jsondata['collection'] = collection

            with open(f"metadata/{name}.json","w") as f:
                f.write(json.dumps(jsondata, indent=4))

            hash_list.append(hash_jsons(f"metadata/{name}.json"))

        generate_final_output(hash_list)


def clean_csv(csv_path):
    '''Fills CSV with Team Names'''
    df = pd.read_csv(csv_path)
    df = df.ffill()
    df.to_csv(csv_path, index=False)


if __name__ == "__main__":
    clean_csv(csv_path)
    func_main(csv_path)
