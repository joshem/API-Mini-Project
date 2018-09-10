#!/bin/bash
python get_twitter_photos.py
ffmpeg -framerate 1/5 -start_number 1000 -i twitterimage%04d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
