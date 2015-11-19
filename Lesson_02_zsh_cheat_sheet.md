# zsh cheat sheet

## Logging in

## Processes

## Navigation

## History

## Printing


## Input / Output

## Fun examples

#####Show all hidden files
`defaults write com.apple.finder AppleShowAllFiles YES`

#####Make the computer talk
`say "Good morning"`

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