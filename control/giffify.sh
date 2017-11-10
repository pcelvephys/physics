#!/bin/bash
DATE=$(date +"%Y/%m/%d")
FILEDAY=$(date +"%Y-%m-%d")
cat /home/chris/flat_images/$DATE/*.png | ffmpeg -y -f image2pipe -r 24 -i -  /home/chris/flat_images/$FILEDAY.gif
