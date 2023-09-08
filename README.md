# oui-miner

Mine IEEE OUI dataset for MAC prefixes for a given vendor

**Example:**

* python3 oui-miner.py huawei
* python3 oui-miner.py huawei -o huawei.csv -v



python3 oui-miner.py -h    
usage: oui-miner.py [-h] [-o OUTPUT] [-v] entity_name

Extract MAC prefixes for a given entity from IEEE OUI list.

positional arguments:
  entity_name           Name of the entity to search for

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output CSV filename
  -v, --verbose         Enable verbose mode 
