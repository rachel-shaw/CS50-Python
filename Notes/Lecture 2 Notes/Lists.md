
<iframe width="560" height="315" 
src="https://video.cs50.io/xdpABsJZQYU" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python

## APPEND, REMOVE from List
results = ["Mario", "Luigi"]

#to add additional items to list
results.append("Princess")

results.append(["Bowser", "Donkey Kong Jr."]) #this adds entire list as grouped LIST
results.remove(["Bowser", "Donkey Kong Jr."]) #let's remove and try another way

results.extend(["Bowser", "Donkey Kong Jr."]) #this adds multiple items correctly  

print(results)


  

### INSERT and REVERSE in List
results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

results.remove("Bowser") #remove's first instance of bowser
# results.append("Bowser") #adds to end of list - not what we want
results.insert(0, "Bowser") #specify location to add him

results.reverse() #to reverse list
  
print(results)
```