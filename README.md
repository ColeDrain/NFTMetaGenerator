## NFT Metadata JSON Generator

### Usage

This package assumes you have python and git installed, if not head over to [Python](python.org) to install
and hed over to [Git Downloads](https://git-scm.com/downloads)

Create a virtual environment with `py -m venv venv`

#### Activate the environment

windows: venv\Scripts\activate
linux: source venv\bin\activate


Then, clone this repo from your terminal with `git clone https://github.com/ColeDrain/NFTMetaGenerator.git` or download manually

If cloning, make sure to change directory: `cd NFTMetaGenerator`

### Install Requirements
pip install -r requirements.txt

Put the CSV containing NFT details in the _csv_ directory, name the file _main.csv_
Then from the root directory, run `py main.py`

For each NFT a metadata.json is generated and stored.
These metadatas are then Hashed and appended to the original CSV

The final output is generated and stored in the _output_ directory as main.output.csv
