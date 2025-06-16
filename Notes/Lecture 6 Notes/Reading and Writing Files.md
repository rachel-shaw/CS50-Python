<iframe width="560" height="315" 
src="https://video.cs50.io/0bCWJjW7SgA" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
"""
Reading and Writing Files
"""

def main():
    with open("src_readwritefiles/alice.txt", "r") as f:
        # contents = f.read() #read whole thing
        contents = f.readlines()

    chapter1 = contents[52:271]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)
    

main()


```