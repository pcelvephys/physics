#!/bin/sh
while true; do  
    echo "Launching ii [$1]..."
    ii -s 192.168.0.10 -p 6667 -n $1 -f &
    iipid="$!"  
    echo "Waiting 5s..."
    sleep 5  
    echo "Joinging #logging..."
    echo "/j #logging" > ~/irc/192.168.0.10/in  
    echo "Waiting for ii to terminate..."
    wait "$iipid"
done  
