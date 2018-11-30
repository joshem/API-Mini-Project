#!/bin/bash


python get_twitter_photos.py $1 $(pwd)

if [ -f "twitterimage1000.jpg" ]; then

	#create video of images using ffmpeg
        ffmpeg -framerate 1/2 -start_number 1000 -i twitterimage%04d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4

	#get image descriptions and output to image_descriptions.txt
	python image_content.py > image_descriptions.txt

	#play video
	ffplay out.mp4
else
        echo "No pictures were downloaded"
fi
