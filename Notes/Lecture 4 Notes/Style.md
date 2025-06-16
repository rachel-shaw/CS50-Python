
<iframe width="560" height="315" 
src="https://video.cs50.io/nbkWuDrl3UI" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
"""
Style: PEP 8 (peps.python.org/pep-0008/)
"""
## SEE students_rs.py script
  
# pylint #style guide checker, but is a bit intense
# pycodestyle #auto reformats your style
# black # opinionated format style
	# run black by typing "black students_rs.py"
	# reformats scripts (can undo but can't redo with control + z)


students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}

for student in students:
  print(student)
```