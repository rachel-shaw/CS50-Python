<iframe width="560" height="315" 
src="https://video.cs50.io/9m1FCOHIIcA" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
import sys
from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        # print(img.size)
        # print(img.format)
        img = img.rotate(180)
		# img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")

main()


```