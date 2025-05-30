
<iframe width="560" height="315" 
src="https://video.cs50.io/iTRBRXOMzeM" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
## USING ITEMS in DICTIONARY

invitees = {
	"Mario":"Princess Peach", "Luigi":"Princess Peach", "Daisy":"Princess Peach", "Yoshi":"Princess Peach"
	}

def main():
	for receiver, sender in invitees.items():
	print(write_letter(receiver, sender))
	
def write_letter(receiver, sender):
	return f"""

	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
		Dear {receiver},
		
		  
		
		You are cordially invited to a ball at Peach's
		
		Castle this evening, 7:00 PM.
		
		  
		
		Sincerely,
		
		{sender}
	
	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
	"""
	
main()


  

## FOR LOOP
names = ["Mario", "Luigi", "Daisy", "Yoshi"]

def main():

for i in range(len(names)):
	print(write_letter(names[i], "Princess Peach"))

def write_letter(receiver, sender):
	return f"""

	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
		Dear {receiver},
		
		  
		
		You are cordially invited to a ball at Peach's
		
		Castle this evening, 7:00 PM.
		
		  
		
		Sincerely,
		
		{sender}
	
	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
	"""
  
main()



## SIMPLFY FOR LOOP
names = ["Mario", "Luigi", "Daisy", "Yoshi"]

def main():
	for name in names:
	print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
	return f"""

	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
		Dear {receiver},
		
		  
		
		You are cordially invited to a ball at Peach's
		
		Castle this evening, 7:00 PM.
		
		  
		
		Sincerely,
		
		{sender}
	
	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
	"""
	
main()
```