# How to write good documentation

When you publish your tools and your project for the world to use and build upon, it is important that you document it well so that others can learn and understand what you did and why. Therefor it is vital to **write proper documentation for your tools**:

### General naming and documentation

- Create a **good name** for the tool
- Put the tool in a **specific subfolder** in your folder
- Add a **README.md** file to that folder
- In the README.md describe all the neccessary elements of documentation:
	- **What** your tool is and what it does
	- **How to install** your tool
	- **Screenshots** of your tool
	- **Examples** how to use your tool
	- **Dependencies** on other tools / python modules / versions of the OS
	- **License** (MIT License)
	
### Document your code
	
- **Split up** your tool into functional blocks of code (with each its own `.py` file?)
- Add a `def main():` to your main python file
- Split up the python file into **well-named** functions
- Add **comments at the top** of each file:
	- The name of the file
	- The author and the license
	- Explanation of what is does in docstring (` """ multiline text """ `)
- Add a **docstring** (`"""..."""`) to each function, explaining:
	- what it does
	- what arguments or parameters it takes
	- what kind of return value it outputs
- Add **comments** (`#`) in your code to explain to yourself and others what the code there does
 
### Document your progress 
 
- Write proper **commit messages** when commit the code and changes to the repository
