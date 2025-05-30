
<iframe width="560" height="315" 
src="https://video.cs50.io/yPyFlO8G6rw" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
def main():

spacecraft = {"name": "James Webb Space Telescope"}
# spacecraft["distance"] = 0.01 #can add here or above by name using comma to separate
spacecraft.update({"distance": 0.01, "orbit": "Sun"})

print(create_report(spacecraft))

def create_report(spacecraft):
	return f"""
	========= REPORT ==========
	Name: {spacecraft.get("name", "Unknown")}
	Distance: {spacecraft.get("distance", "Unknown")} AU
	Orbit: {spacecraft.get("orbit", "Unknown")}
	===========================

	"""

main()
```


```python
# USING KEYS
distances = {
	"Voyager I": 163,
	"Voyager II": 136,
	"Pioneer 10": 80,
	"New Horizons": 58,
	"Pioneer II": 44
}

def main():
	for name in distances.keys():
	print(f"name is {distances[name]} AU from Earth")

  

main()
```

```python
## USING VALUES
distances = {
	"Voyager I": 163,
	"Voyager II": 136,
	"Pioneer 10": 80,
	"New Horizons": 58,
	"Pioneer II": 44
}


def main():
	for distance in distances.values():
	print(f"{distance} AU is {convert(distance)} m")

def convert(au):
	return au * 14959780700

main()
```