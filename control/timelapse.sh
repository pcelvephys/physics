#!/bin/bash
cat /tank/data/timelapse/*.png | ffmpeg -y -f image2pipe -r 15 -i -  ./15fps.mp4
