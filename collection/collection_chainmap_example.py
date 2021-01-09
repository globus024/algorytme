import argparse
from collections import ChainMap

default = {'ip': 'localhost', 'port': 80}
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip')
parser.add_argument('-p', '--port')
args = parser.parse_args()
new_dict = {key: value for key, value in vars(args).items() if value}
print(new_dict)
setting = ChainMap(new_dict, default)
print(setting['ip'])
print(setting['port'])
print(args)
