
<iframe width="560" height="315" 
src="https://video.cs50.io/2hsn7AxXKmg" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
##use print to debug
def main():
	height = int(input("Height: "))
	pyramid(height)

def pyramid(n):
	for i in range(n):
		print(i, end="")
		print("#" * (i+1))

if __name__ == "__main__": #for larger files where you only want to run main?
main()

  
  

##use debugger
def main():
	height = int(input("Height: ")) #step over (don't need to look at int function as we didnt write it)
	pyramid(height) #step into

def pyramid(n):
	for i in range(n): #step over
		print("#" * i) #step over

if __name__ == "__main__": #for larger files where you only want to run main?
main() ## set breakpoint here, step into

```