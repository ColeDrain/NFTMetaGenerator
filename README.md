## NFT Metadata JSON Generator

### Usage

First, clone this repo from your terminal with `git clone https://github.com/ColeDrain/NFTMetaGenerator.git` or download manually

If cloning, make sure to change directory: `cd NFTMetaGenerator`

Put the CSV containing NFT details in the _csv_ directory, name the file _main.csv_
Then from the root directory, run `py main.py`

For each NFT a metadata.json is generated and stored.
These metadatas are then Hashed and appended to the original CSV

The final output is generated and stored in the _output_ directory as final_output.csv
