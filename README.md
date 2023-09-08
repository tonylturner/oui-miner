# OUI-Miner

`oui-miner` is a Python tool designed to mine the IEEE OUI dataset for MAC prefixes associated with a specified vendor.

## Introduction

OUI, which stands for Organizationally Unique Identifier, is used in the MAC addresses to signify the manufacturer or vendor of the network device. With `oui-miner`, you can easily extract the MAC prefixes for a given vendor from the official IEEE OUI list.

## Features
- Fetch data from the official IEEE OUI list.
- Extract MAC prefixes for a specified vendor or manufacturer.
- Save the extracted MAC prefixes to a CSV file.
- Print the results directly to the console.
- Verbose mode for detailed error handling.

## Prerequisites
- Python 3.x
- Required Python libraries: `requests`, `csv`, `argparse`, `re`

## Usage

Basic usage:
```bash
python3 oui-miner.py <vendor_name>
```
