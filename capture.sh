#!/bin/bash

INTERFACE=eth0
OUTPUT=traffic.pcap

echo "Starting packet capture..."

sudo tcpdump -i $INTERFACE -w $OUTPUT