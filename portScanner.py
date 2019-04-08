#!/usr/bin/env python3
#author:kin

import argparse
from lib.SYNscan import portScan

parser = argparse.ArgumentParser(description="This is a port scan script.")
parser.add_argument('--port', '-P', dest='ports', type=str, help='the ports we will scan')
parser.add_argument('--host', '-H', dest='host', type=str, help='the host we will scan.')
args = parser.parse_args()

targetHost = args.host
targetPorts = args.port.split(',')

if (targetHost == None) or (targetPorts == None):
    print(parser.usage)
    exit(1)
else:
    portScan(targetHost, targetPorts)