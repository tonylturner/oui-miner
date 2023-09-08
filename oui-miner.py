import requests
import csv
import argparse
import re
import sys

URL = "https://standards-oui.ieee.org/oui/oui.txt"

def fetch_data(url):
    response = requests.get(url)
    print("Data fetched from the URL.")
    return response.text

def extract_data(entity_name, data):
    lines = data.split("\n")
    entity_data = []
    
    print("Parsing the data...")
    
    pattern = r'\b' + re.escape(entity_name.upper()) + r'\b'

    for i, line in enumerate(lines):
        if re.search(pattern, line.upper()) and '(base 16)' in line:
            hex_value = lines[i-1].split()[0]
            entity = line.split('\t\t')[1]
            entity_data.append([hex_value, entity])
    
    if not entity_data:
        print(f"No MAC addresses found for {entity_name}.")
    return entity_data

def save_to_csv(entity_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['MAC Prefix', 'Entity Name'])
        csvwriter.writerows(entity_data)
    print(f"Data saved to {filename}")

def print_to_stdout(entity_data):
    print("MAC Prefix,Entity Name")
    for item in entity_data:
        print(f"{item[0]},{item[1]}")

def main():
    parser = argparse.ArgumentParser(description='Extract MAC prefixes for a given entity from IEEE OUI list.')
    parser.add_argument('entity_name', type=str, help='Name of the entity to search for')
    parser.add_argument('-o', '--output', type=str, default=None, help='Output CSV filename')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode for error handling')

    args = parser.parse_args()

    try:
        data = fetch_data(URL)
        entity_data = extract_data(args.entity_name, data)
        if entity_data:
            if args.output:
                save_to_csv(entity_data, args.output)
            else:
                print_to_stdout(entity_data)
    except Exception as e:
        if args.verbose:
            print(f"An error occurred: {str(e)}")
        else:
            print("An error occurred. Run with -v for more details.")

if __name__ == "__main__":
    main()
