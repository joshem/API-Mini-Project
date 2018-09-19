#!/bin/bash
python get_twitter_photos.py
if [ -f "twitterimage1000.jpg" ]; then
        ffmpeg -framerate 1/2 -start_number 1000 -i twitterimage%04d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
	python image_content.py
else
        echo "No pictures were downloaded"
fi

