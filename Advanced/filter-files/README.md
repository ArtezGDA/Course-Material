# Filter Files

These are example scripts that can be given one or more files on the command line. The script then filters these files and outputs some interesting results. There are three variants of this script, in increasing-complexity order:

- `files_input.py`: outputs the first line of each file you give it
- `find_md_links.py`: assumes input are `.md` files, and prints all the links in these markdown files
- `find_md_links_color`: same as above, but adding some nice colors to the output

And then there is an Advanced section which does even more with these links.

## `files_input.py`

Takes all the arguments you give in on the command line. If these argument are files and these files are not empty, it outputs the name of the file and the first line of the file itself.

As example, run it using the following:

`python ./files_input.py file1.txt file2.txt file3.txt`

or:

`python ./files_input.py file*.txt`

or in the case of this directory:

`python ./files_input.py *.md`

## `find_md_links.py`

As before, but now assumes that all the files given are in the markdown format. The script will then search these given files for markdown formatted links (`[title of the link](url_or_markdown_file)`), and print them to the standard out.

As example, it can be executed by running the following command:

*(assuming you're in the root directory of the Course Material)*  
`find . -name '*.md' | xargs python ./Basics/filter-files/find_md_links.py`  

(This searches for all the `.md` files from the current directory, and then send the output of these files to this script).

## `find_md_links_color.py`

As the example before, this script can be given one or more files on the command line, and finds all the markdown formatted links in them.

Additionally it adds nice colors to the output.

In order to run this third example, you need to install the **colored** python module with:

`sudo easy_install colored`
