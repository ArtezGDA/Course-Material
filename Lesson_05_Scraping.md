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

Print out a list of repositories you can commit to:

```
for repo in g.get_user().get_repos():
	print repo.name
```

So what exactly happens here? And where is the documentation? Let's break these two lines up into smaller bits:

- `for e in a_collection:` should be recognized as familiar *for loop*
- `g.get_user()`: a method `get_user()` on the Github instance `g` of above.
	- Let's find the documentation of this method. It's part of the [**Main class: Github** reference](http://pygithub.readthedocs.org/en/latest/github.html)
	- Jump to the section about the [`get_user()`](http://pygithub.readthedocs.org/en/latest/github.html#github.MainClass.Github.get_user) method
	- You see that it returns a `github.NamedUser.NamedUser` object. Open the documentation on [NamedUser](http://pygithub.readthedocs.org/en/latest/github_objects/NamedUser.html)
- `.get_repos()`: is a method called on this NamedUser object.
	- Read the documentation on the [`get_repos()`](http://pygithub.readthedocs.org/en/latest/github_objects/NamedUser.html#github.NamedUser.NamedUser.get_repos) method
	- You see the return type is a `github.PaginatedList.PaginatedList` of `github.Repository.Repository`s
	- The *Paginated List* means that it will not return these repositories all in once, but in smaller quanties (pages), so the network and other systems can manage giant lists more easily. Luckily for us, we can still just use *Paginated Lists* like in a for loop, like we do with *lists*.
- Inside the for loop the `repo` variable represent each repository in turn.
	- Open the documentation from the [`github.Repository.Repository`](http://pygithub.readthedocs.org/en/latest/github_objects/Repository.html) link from above.
	- Find the `name` property: [`name`](http://pygithub.readthedocs.org/en/latest/github_objects/Repository.html#github.Repository.Repository.name)
	- And see what other things can be found out about a repository.
	
### Get a list of all commit (for a single repository)

- Get a repository (`g.get_repo()`)
	- (full_name!) and what goes wrong if you take the name
- Use tab complete (ipython) to see the possibilities
- Get the commits (`repo.get_commits()`) -> `github.PaginatedList.PaginatedList` of `github.Commit.Commit`
- Get one commit and investigate `ci = repo.get_commits()[0]` (most recent commit)
- ci. tab to autocomplete
- Read the documentation. ... Relalize there are two types: `github.Commit.Commit` and `github.GitCommit.GitCommit`. We want the latter
- `gc = ci.commit`
- Investigate that gc object. See we have
	- author
	- last_modified (which is probably a date)
	- message
	- parent (if we which to draw a graph from this)
- Message and last_modified are straight forward, but what about the author?
- Investigate the `github.GitAuthor.GitAuthor` model. Is has
	- name
	- email
- Let's use the name

### Write this all out in a python script

```
	# Setup
	from github import Github
	from secret_password import github_account

	g = Github(github_account['user'], github_account['password'])
	
	# Get the repository from its full name
	repo = g.get_repo('ArtezGDA/Algorithmic-Nature')
	
	# Iterate through all commits
	for commit in repo.get_commits():
	
		# Get the required information
		gc = commit.commit # GitCommit object
		author_name = gc.author.name
		time_modified = gc.last_modified
		message = gc.message
		
		# print the results
		print "%s - %s: %s" % (time_modified, author_name, message)"
```
