
<iframe width="560" height="315" 
src="https://video.cs50.io/COWxTAPkr_k" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
  

def main():
	phone = "617-495-1000"
	print(phone[0:3]) #can use indexes to find area code (3 b/c up to but not including last number)
	print(phone[:3]) #also works if want first index
	print(phone[8:]) #last four digits through last index
	print(phone[-4:]) #last 4

main()

```