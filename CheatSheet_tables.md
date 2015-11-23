## Navigation

| Command      | Shortcut   | Result                                                                                    |
|:-------------|:-----------|:------------------------------------------------------------------------------------------|
| `cd`         |            | ***C**hange **D**irectory*: go to the directory (needs a *path* as argument)              |
| ⇥            |            | Use the **tab** key to *autocomplete*                                                     |
| `ls`         |            | ***L***i***s***t files in current directory                                               |
| `ls -l`      | `l`        | List files with *long format*                                                             |
| `ls -al`     | `ll`       | List *all* files in long format                                                           |
| `pwd`        |            | ***P**rint **W**orking **D**irectory*: see the current path                               |
| ``pwd `.` `` | `.`        | Go to the current directory (useful if you're there via symlink)                          |
| `mkdir`      |            | ***M**a**k**e **Dir**ectory*                                                              |
| `mkdir -p`   | `md`       | Create Directories up to path and create steps inbetween                                  |
| `rmdir`      | `rd`       | ***R**e**m**ove **Dir**ectory*                                                            |
| `which`      |            | Tells you which command will be executed or where the *executable* is located.            |

| Keyword | Meaning                       | Example                                                                     |
|:--------|:------------------------------|:----------------------------------------------------------------------------|
| `~`     | Home directory                | `cd ~` or `cd ~/Desktop`                                                    |
| `.`     | Current directory             |                                                                             |
| `..`    | Parent directory              | `cd ..` or `cat ../../../file.txt`                                          |
| `/`     | Root directory                | `cd /` or `ls /Volumes`                                                     |
| `?`     | Single wildcard character     | use `T?m.md` to find *Tim.md*, *Tom.md* or *Tam.md*, but not *Theorem.md*   |
| `*`     | Multiple wildcard characters  | `ls *.png` to list all .png files in the current directory                  |

| Command          | Shortcut   | Result                                                                                |
|:-----------------|:-----------|:--------------------------------------------------------------------------------------|
| `cd ..`          | `cd..`     | Go to the (1 level up) parent directory                                               |
| `cd ../..`       | `cd...`    | Go to the (2 levels up) grand-parent directory                                        |
| `cd ../../..`    | `cd....`   | Go to the (3 levels up) grand-grand-parent directory                                  |
| `cd ../../../..` | `cd.....`  | Go to the (4 levels up) grand-grand-grand-parent directory                            |
| `cd -`           | `1`        | Go to the previous directory (in your history)                                        |
| `cd +2`          | `2`        | Go to 2 directories ago                                                               |
| `cd +3`          | `3`        | Go to 3 directories ago                                                               |
| `cd +4`          | `4`        | Go to 4 directories ago                                                               |
| `cd +5`          | `5`        | Go to 5 directories ago                                                               |
| `cd +6`          | `6`        | Go to 6 directories ago                                                               |
| `cd +7`          | `7`        | Go to 7 directories ago                                                               |
| `cd +8`          | `8`        | Go to 8 directories ago                                                               |
| `cd +9`          | `9`        | Go to 9 directories ago                                                               |
| `dirs -v`        | `d`        | Display all the previous directories                                                  |

## File Handling

| Keyword | Meaning                                | Example                                                             |
|:--------|:---------------------------------------|:--------------------------------------------------------------------|
| `cp`    | ***C**o**p**y*                         | `cp file.txt ~/Desktop` or `cp file.txt file2.txt` (does duplicate) |
| `mv`    | ***M**o**v**e*                         | `mv file.txt ~/Desktop` or `mv file.txt file2.txt` (does rename)    |
| `touch` | Make new file or set modification date | `touch empty.txt`                                                   |
| `ln`    | ***L**i**n**k*: make alias             | `ln -s ~/Documents/MediaDesign/text-IO/Dirk/ ~/Desktop/textio`      |
| `rm`    | ***R**e**m**ove*: delete a file        | **NOTE!**: `rm` hard deletes a file directly. (no way to undo)      |

## Logging in

| Command  | Meaning                                           | Example                                                 |
|----------|---------------------------------------------------|---------------------------------------------------------|
| `ssh`    | ***S**ecure **Sh**ell*: log into somewhere remote | `ssh local@domain_of_other_computer.somewhere`          |
| `whoami` | Display as who you are currently logged in        |                                                         |
| `logout` | To log out of the current shell                   |                                                         |
| `sudo`   | ***Su**peruser **Do***: do as admin               | `sudo mkdir /Library/Logs/Test`                         |

## Processes & Inspection

| Command    | Meaning                           | Example                                                                  |
|------------|-----------------------------------|--------------------------------------------------------------------------|
| `ps`       | Show running processes            | `ps -ax` Show *all* processes as root                                    |
| `top`      | Show the most consuming processes | This is live. Type `Q` to quit.                                          |
| `df`       | ***D**isplay **F**ree* disk space |                                                                          |
| `du`       | Display ***d**isk **u**sage*      | `du -hs *` Display the file and directory sizes of the current directory |
| `ifconfig` | See your network interfaces       | The type of network your connected to (wifi, bluetooth, etc)             |
| `netstat`  | See the live network connections  | `netstat -a` List all current connections.                               |

## History

| Command               | Shortcut | Meaning                                                                        |
|-----------------------|----------|--------------------------------------------------------------------------------|
| `history`             |          | Display the history of commands                                                |
| `history 1 | grep $@` | `gh`     | ***G**rep **H**istory*: search history of commands for anything with this word |

arrow up/down for history
alt . for previous last word
ctrl r (search history)
!!
!abc
!123

- pijljes / alt . / history / gh / !! nn

## Command Line Navigation

alt click for cursor
ctrl a / ctrl e
ctrl k (clear up to carrot)
alt b / f 

## Printing

- echo / cat / more / tail / man 

navigation in more/less:
     ^f
     ^b
     /
     n
	 N

## Finding stuff

grep
     -c
     -n
find
     find . -name "*.txt"
     find . -type d "m*"

grep
find
locate

## Input / Output


|           (pipe)
>          (redirect)
>>        (append)
<          (file input)
``    (backticks)

pbcopy
pbpaste
open .
