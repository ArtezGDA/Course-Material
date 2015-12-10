# Setup
from github import Github
from secret_password import github_account
import json

g = Github(github_account['user'], github_account['password'])

# Get the repository from its full name
repo = g.get_repo('ArtezGDA/Algorithmic-Nature')

# Store all commits in a list of dicts
commitsList = []

# Iterate through all commits
for commit in repo.get_commits():
	
	# Create an empty dict
	commitDict = {}
	
	# fill the dict with the desired information
	gc = commit.commit # GitCommit object
	commitDict['author_name'] = gc.author.name
	commitDict['last_modified'] = gc.last_modified
	commitDict['message'] = gc.message
	
	# Append the new dict to the list
	commitsList.append(commitDict)
	
	# Print some info as progress.
	# This step is not needed, but without printing progress, you do not know if the script has crashed or still is busy.
	print "read commit by %s" % (gc.author.name)
	
# Save as json
jsonfile = "all_commits.json"
with open(jsonfile, 'w') as outputFile:
	json.dump(commitsList, outputFile)
