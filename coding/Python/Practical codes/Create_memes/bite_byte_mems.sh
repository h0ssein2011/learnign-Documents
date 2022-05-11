#! /bin/bash

word="rabbit"

img_url=`./dl_photo_from_google.py $word` 
# echo "Image URL: $img_url"
wget $img_url -O tmp.png
convert tmp.png -resize 200x200 tmp.png
magick tmp.png -tile 1x1  -title $word top.png
magick tmp.png -tile 4x2  -title $word tmp.png tmp.png tmp.png tmp.png tmp.png tmp.png tmp.png tmp.png bottom.png


