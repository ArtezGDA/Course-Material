# Install Qt5 as matplotlib engine

### Why would you want this?

You could sometimes experience a problem with closing matplotlib windows ... or regaining access to the iPython prompt. The symptoms are that you can not close a window opened with `imshow()` and when you force quit the _Python Launcher_ process, also the ipython interactive interpretor quits.

### Summary

We can fix this by changing the *backend* of matplotlib, i.e. the application framework (graphics and interactive) that matplotlib is using to open with window and listen to user events. We're gonna change the backend from the "native" Mac OS X python engine to Qt5, ([Qt](https://www.qt.io), version 5).

#### Warning: difficulty ahead

The following steps are really specific for my current version of software: python 2.7 and Mac OS X 10.11 El Capitan. It took me a few steps back and forth to finally make this work. **So, if your system is different, it might be that these steps are not so straight forward**, or that you don't need some steps. The only way to make this work on your machine, is if **you have patience, experience with working on the command line, and are not scared of reading error messages**, forum posts and trying out different versions of the various software elements. 

## Installation steps for PyQt5 with python 2.7 on Mac OS X 10.11 El Capitan

Roughly I'm following this tutorial:

- https://fredrikaverpil.github.io/2015/11/25/compiling-pyqt5-for-python-2-7-on-os-x/

But then modified specifically to my system:

- When I tried this the lastest version of Qt5 was Qt 5.8.1. but that seemed incompatible with the latest version of sip-4.18. So we needed Qt 5.7.
- And the installation directories were slightly different on my machine (running Mac OS X El Capitan).  
  So you need to know where homebrew is installing its formulas. In my case that is:
  - */usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula*
- Also you need to know where python installs its modules (the *site-packages* directory):
  - */usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages*
  - on my system this path is also stored in the $PYTHONPATH variable

### Install wget

(Assuming you already have python installed through `brew`)

`brew install wget`

(Also assuming you already have Xcode tools installed)

### Install Qt5 (version 5.7.1_1)

From reading the logs of homebrew's qt5 formulas. (`brew log qt5`), I found the latest revision of the Qt 5.7. 

- use commit 805b2e0b0201b2560235eb3ee5c724d241ba42d5 of homebrew's qt5 formula:
  - `cd /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/`
  - `git checkout 805b2e0b0 Formula/qt5.rb`
  - `brew install qt5`

### Get the source for *PyQt5* and *SIP*

```
wget http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.6/PyQt5_gpl-5.6.tar.gz
wget http://freefr.dl.sourceforge.net/project/pyqt/sip/sip-4.18/sip-4.18.tar.gz
```

### Install SIP 

```
tar -xvf sip-4.18.tar.gz
cd /sip-4.18
python configure.py -d $PYTHONPATH
make
make install
```

### Prepare to install PyQt5

```
cd..
tar -xvf PyQt-gpl-5.6.tar.gz
cd PyQt-gpl-5.6
```

### Fix Qt's `configure.py` script to not check compatible licenses

When following Fredrik Averpil's steps, I was hit by the following error:

```
Error: This version of PyQt5 and the commercial version of Qt have incompatible licenses
```

Probably there are other, better, more (legally) correct ways to solve this issue. Or maybe this is error is just the result of not-yet updated licenses on one side. In any case, the easiest way to solve this, and not be bothered by it, is to remove the check for compatible licenses:

- Modify PyQt5_gpl-5.6/configure.py 
  - find the line that says "This version of PyQt5 and the commercial version of Qt have"
  - identify the 4 lines `if` block doing the licenses check
  - and comment it out those 4 lines

### Continue the installation of  PyQt5

The `python configure.py ...` line for PyQt5 is the longest command to type in. As you'll see it consists of a lot of parts (and paths) and they all need to be correct.

Those parts are:

- `-d $PYTHONPATH` : this path needs to point to your python's `site-packages` directory
- `--qmake=/usr/...` : this needs to point to the `qmake` executable (binary) that you created using `brew install qt5`
- `--sip=/usr/...` : this needs to point to the `sip` binary that you created when installing SIP
- `--sip-incdir=../sip-4...` : this needs to point to the `lib` directory in the source code directory of SIP

Combined, that makes on my machine:

```
python configure.py -d $PYTHONPATH --qmake=/usr/local/Cellar/qt5/5.7.1_1/bin/qmake --sip=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin/sip --sip-incdir=../sip-4.18/siplib
```

If you have it configured correctly, you can `make` and `make install` it. But do note that these two last steps can take about 30 minutes of compiling and building. Be patient.

- `make`
- `make install`

### Test the installation

`ipython`

*>>>* `import PyQt5`

### And then you can use it with:

`ipython --matplotlib=qt5`

or 

`ipython`

*>>>* `%matplotlib qt5`


