#!./.venv/bin/python
import os
import sys
import argparse

parser = argparse.ArgumentParser(
                    prog='Job Sample')
parser.add_argument('-o', '--output')
parser.add_argument('-v', '--value')
parser.add_argument('-p', '--process')
args = parser.parse_args()
print(args)

os.makedirs("./result", exist_ok=True)
with open(f"result/o={args.output}-p={args.process}.txt", "w") as fp:
    fp.write(f"{args.value}\n")
    fp.write(f"{sys.executable}\n")
    fp.write(f"{sys.version}\n")
