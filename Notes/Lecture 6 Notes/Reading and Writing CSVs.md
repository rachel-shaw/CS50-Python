<iframe width="560" height="315" 
src="https://video.cs50.io/VRbkyEFCqZo" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
"""
Reading and Writing CSVs Shorts
"""
"""read brightness from each file"""
import csv
import numpy as np
from PIL import Image

def main():
    with open("src_readwritecsvs/views.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            brightness = calculate_brightness(f"src_readwritecsvs/{row['id']}.jpeg")
            # print(row["id"])
            print(round(brightness, 2))

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

"""create new csv with brightness column (read + write two separate files at same time)"""
import csv
import numpy as np
from PIL import Image

def main():
    with open("src_readwritecsvs/views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames = reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"src_readwritecsvs/{row['id']}.jpeg")
            writer.writerow(
                {
                    "id": row["id"], 
                    "english_title": row["english_title"], 
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2)
                }
            )


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

"""write code more efficiently"""
import csv
import numpy as np
from PIL import Image

def main():
    with open("src_readwritecsvs/views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames = reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"src_readwritecsvs/{row['id']}.jpeg"),2)
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()


```