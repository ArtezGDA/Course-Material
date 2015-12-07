# Lesson 05: Scraping

### Introduction

Scraping the automatic collection (and possibly organization) of big quantities of data, often from online sources.

Examples of tasks you might wish to execute using scraping:

- Find all occurances of the word 'horror' in the collected works of Edgar Allan Poe.
- Find all links and references in a set of markdown files.
- Find the box office revenues of all Disney movies.
- Collect all commit messages from a repository on github.

### Process

The process of scraping can be compared to the process of mine a rare ore:

*Acquire* -> *Parse* -> *Filter* -> *Organize*

1. **Acquire** - Automatic collection of huge quantites of data
2. **Parse** - Interpret the data as content. (e.g. parse the html into useful values)
3. **Filter** - Filter the information and only keep what is looked for
4. **Organize** - Collect these bits of information into a coherent set

### Examples

- [scrape Disney's box office from Wikipedia](https://github.com/ArtezGDA/python-web-scraper)
- [json reading and writing](https://github.com/ArtezGDA/Course-Material/tree/master/Basics/json)
- [find links in markdown files](https://github.com/ArtezGDA/Course-Material/tree/master/Basics/filter-files)
- use an API ...

## GitHub API

An API (Application Programming Interface), is a layer of access (and interactivity) which can be used by developers to gather data. The data is often similar to the data you can gather from just visiting the services' website or by using the app. The difference is that an *API* allows this process to be automated, so computers can talk to computers, instead of humans talking to computers or vice versa.

### Documentation

A quick online search for `Github API` brings you to the official API page:  
[GitHub API v3 | GitHub Developer Guide](https://developer.github.com/v3/)

This API is the most basic form of their API, which works with simple HTTP GET requests, and parsing the response. The benefit of such a HTTP API, is that is so simple that every type of device or language can use this.

For our case, we want to look a bit further and go look for a Python API.

### Python API 

There are a few different Python libraries which can be used as python wrapper around the Github API, but the one with the most traction at the moment is [PyGithub](https://github.com/PyGithub/PyGithub)

As with more and more tools, its documentation is hosted elsewhere, at [readthedocs.org](http://pygithub.readthedocs.org/en/stable/)

### Installation

From this documentation, click on the **Introduction**, then **Download and install**. So we can use the familiar `easy_install`:

`sudo easy_install PyGithub`

### User + Password

The tutorial starts with the following. Importing the module and create a Github instance from a *user* and *password*:

```
from github import Github

g = Github("user", "password")
```

Ofcourse you should replace the *user* and *password* with a valid username and password for Github. But there are two major security issues with just using your normal Github password:

1. This is your root password for everything on Github, so also editing, deletion and changing your profile. You do not want scraping script to be able to do this. What if you make a mistake?
2. You surely DO NOT want to publish your password online. (Which is what you will be doing when you put your scraping script on Github again)

So we need to be safe and find a secure way around these threats.

#### Step 1: Create a special password for this usage.

1. Click to your avatar icon in the top right corner of a page on Github
2. Go to **Settings**
3. Select **Personal access tokens** from the left column
4. Click on **Generate new token**
5. Type in your password
6. Select a few necessary scopes (repo, public repo, user:email, repo:status) and give this token a name e.g. "Github from python"
7. Click **Generate token**
8. Copy the resulted token and store it in a safe file

By selecting the scopes you made sure this password can only be used for a limited set of actions, you approved off. Further more, if you're done with it or the password might have been compromised, you can just toss it away and create a new one.

#### Step 2. Make sure you do not commit the token.

Committing secret keys, tokens and passwords is really the very last thing you want to do. So let's make sure it doesn't happen. The best trick is to store the token in a seperate file, and make sure the file is never added to Github.

1. Create a new file called `secret_password.py`
2. In that file create a dictionary like the following:
	```
	github_account = {'user': "your_user_name", 'password': "the_token_1234abcdef9876543210"}
	``` 
3. Use this to get access to GitHub from your script. The example now is as follows:
	```
	from github import Github
	from secret_password import github_account

	g = Github(github_account['user'], github_account['password'])
	```
4. To make sure the password file is not accidently added to Github, add the file to the git ignores. (The git ignores is a set of files you want to have ignored from the git system, so they are not added or updated. Warning, these ignores can still be added if you really wish to do so, so keep making sure you don't add them later).
5. Create a file called `.gitignore` and add the following in it:
	```
	# ignore these files and patterns
	secret_password.py
	```
6. Type `git status` to verify that the password file won't be committed but the `.gitignore` will.

### Continue the tutorial

Print out a list of repositories you commit to:

```
for repo in g.get_user().get_repos():
	print repo.name
```
