#! /bin/bash

word="rabbit"

img_url="$./dl_photo_from_google.py $word" 
wget $image_url -O word.png
convert word.png -resize 200x200 word.png