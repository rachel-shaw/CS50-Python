## Set Up Python & Conda
- To install function code:
	- Press **Cmd + Shift + P**
	- Type and select `Shell Command: Install 'code' command in PATH`
- To install python
	- download python
	- **Cmd + Shift + P** --> `Python: Select Interpreter`
	- Paste this path: */Library/Frameworks/Python.framework/Versions/3.13/bin/python3*
	- Select *conda* for environment
- To install conda
	- download and install anaconda
	-` nano ~/.zshrc`
	- `conda deactivate`
	- `conda --version`
	- *(base)* is added before folder to show it is active
	- possibly some other steps between but finally got it to work
	
## Connecting VS Code Directory to Sharkology
- **To change directory:** cd "/Volumes/Rachel/GitHub Repos/CS50-Python"
- **To list files in that folder**: ls
- **To run**: python hello.py
- **Clear terminal screen**: Command (⌘) + K
- **To save**: Command (⌘) + S (white circle on file name shows changes have been made that need to be saved)
- **Annotate**: Command (⌘) + /
- **Comments**: """ instead of #
- Tab to finish typing


### Code Language
- example of a *function* is print
- functions can take in *arguments*, written using *parameters* (same thing, different viewpoint)
	- ex) sep and end in print function = parameters
