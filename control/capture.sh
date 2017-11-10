#!/bin/bash
fswebcam --frames 1 --resolution 1920x1080 --png 0 /home/lab/timelapse/`date +"%m-%d-%Y_%H-%M-%S"`.png
