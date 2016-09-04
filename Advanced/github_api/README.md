# Github API

### Example of scraping from Github

In this example we want to scrape some information from Github, in an automated way. To do that we'll use the [`PyGithub`](https://github.com/PyGithub/PyGithub) python module, which wraps around the Github API v3.

As an example this script will scrape all the commits from a single repository. From each commit it will read its author and the commit message. And it will then creates a `.json` file with all the collected data in.

### Dependencies

To make this script work, you'll need the `PyGithub` module. To install that use:

`sudo easy_install PyGithub`

### Usage

#### User + Password

And this script also needs a password file. (Which for obvious reasons is not commited):

1. In the same directory as this script, create a new file called `secret_password.py`
2. In that file create a dictionary like the following:  
	```python
	github_account = {'user': "your_user_name", 'password': "the_token_1234abcdef9876543210"}
	``` 
	
#### Choose a repository

If you have that, you might want to change the repository that it scrapes. Look at `scrape_commits.py`, line 9:

`repo = g.get_repo('ArtezGDA/Algorithmic-Nature')`

And change that full name for other repositories.

#### Running the script creates a `.json` file

If you run this script with:

`python scrape_commits.py`

it will create a file `all_commits.json` will all the commit messages
