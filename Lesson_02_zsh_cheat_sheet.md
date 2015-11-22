## Setup

#### Install Z-shell and the dotfiles

Get the dotfiles from [zsh-dotfiles](https://github.com/irlabs/zsh-dotfiles) on github and follow its install guide.

- set **zsh** as your default shell
- install the dotfiles
- enable the alt key as meta key

####General Note:
#####Avoid spaces in names of files or directories

It is good practice to avoid spaces ` ` in names of files or directories. Spaces can be used in the command line by *escaping* them with a `\ `: e.g. `cd Classes/Media\ Design/Homework`. But this is easy to forget and then cause errors. Because real spaces have different behavior: e.g. `touch Media Design` creates **two** files: one called *Media*, the other called *Design*.

Also spaces in url or file names on websites are likely to break. (Again, spaces can be *escaped* by using `%20`, but this is far from convenient)

Instead of spaces, use underscores (`_`), dashes (`-`), or **C**amel**C**asing.

----

# zsh cheat sheet

## Navigation


| Command      | Shortcut | Result                                                                         |
|--------------|----------|--------------------------------------------------------------------------------|
| `cd`         |          | ***C**hange **D**irectory*: go to the directory (needs a *path* as argument)   |
| ⇥            |          | Use the **tab** key to *autocomplete*                                          |
| `ls`         |          | ***L***i***s***t files in current directory                                    |
| `ls -l`      | `l`      | List files with *long format*                                                  |
| `ls -al`     | `ll`     | List *all* files in long format                                                |
| `pwd`        |          | ***P**rint **W**orking **D**irectory*: see the current path                    |
| ``pwd `.` `` | `.`      | Go to the current directory (useful if you're there via symlink)               |
| `mkdir`      |          | ***M**a**k**e **Dir**ectory*                                                   |
| `rmdir`      |          | ***R**e**m**ove **Dir**ectory*                                                 |
| `which`      |          | Tells you which command will be executed or where the *executable* is located. |
| `cd -`       | `1`      | Go to the previous directory (in your history)                                 |
| `cd +2`      | `2`      | Go to 2 directories ago                                                        |
| `cd +3`      | `3`      | Go to 3 directories ago                                                        |
| `cd +4`      | `4`      | Go to 4 directories ago                                                        |
| `cd +5`      | `5`      | Go to 5 directories ago                                                        |


| Keyword | Meaning                       | Example                                                                     |
|---------|-------------------------------|-----------------------------------------------------------------------------|
| `~`     | Home directory                | `cd ~` or `cd ~/Desktop`                                                    |
| `.`     | Current directory             |                                                                             |
| `..`    | Parent directory              | `cd ..` or `cat ../../../file.txt`                                          |
| `/`     | Root directory                | `cd /` or `ls /Volumes`                                                     |
| `?`     | Single wildcard character     | use `T?m.md` to find *Tim.md*, *Tom.md* or *Tam.md*, but not *Theorem.md*   |
| `*`     | Multiple wildcard characters  | `ls *.png` to list all .png files in the current directory                  |

## Logging in


## Processes

## History

- pijljes / alt . / history / gh / !! nn

## Printing

- echo / cat / more 

## Input / Output

## Fun examples

#####Show all hidden files

`defaults write com.apple.finder AppleShowAllFiles YES`

(Use `NO` instead of `YES` to hide them again.)

The *defaults* command allows you to see and change application and system preferences. It also allows you to change settings for which there is no interface in the Preferences menu.

#####Star Wars in ASCII-art

`telnet`  
`o`  
`towel.blinkenlights.nl`  
...  
`^]`  
`quit`

#####Doktor Eliza

`emacs`  
`(ESC)`  
`X`  
`doctor`  
...  
`^x^c`  

#####Dunnet Adventure

`emacs`  
`(ESC)`  
`X`  
`doctor`  
`look` / `take shovel` / `east` / `dig` / `inventory` ...
...  
`^x^c`  

----

For the following you will need **Homebrew**. Install `brew` from the [Homebrew](http://brew.sh/index.html) website: 

----

#####Fortune

Install with  

`brew install fortune`  

Use:  

`fortune`

#####Cowsay

Install with  

`brew install cowsay`  

Use:  

`cowsay "Moo"`  

List all possible characters:  

`cowsay -l`  

Combine with fortune:  

`fortune | cowsay`

----

#####Make the computer talk

`say "Good morning"`

Use a different *voice* with the `-v` argument:
 
`say -v Victoria "Good morning"`

Use the following to see all the voices available  

`say -v '?'`

