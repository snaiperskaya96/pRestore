# pRestore
pRestore is a disaster-recovery script which is meant to restore all the known files and directories permissions back to previous pRestore backups

<p align="center">
<b><a href="#overview">Overview</a></b>
|
<b><a href="#features">Features</a></b>
|
<b><a href="#installation">Installation</a></b>
|
<b><a href="#examples">Examples</a></b>
|
<b><a href="#license">License</a></b>
</p>

<br>

## Overview

It may happens - and crap, it happens - that sometimes we just screw up permissions.

Long story short: what made me make this was basically a cool **chmod -R 775 /** fired by _a friend of mine_ on a test server
making it unreachable and probably unusable.

<p align="right"><a href="#top">:arrow_up:</a></p>

## Features

No more than what have been already said:
- **Recursively searches inside the target directory and save every file permissions (owner and group included)**
- **Runs on both Unix and OSX**

<p align="right"><a href="#top">:arrow_up:</a></p>

## Installation

Quite easy.

Clone the repository, enter the folder via a shell, and run:

```console
# python2.7 main.py -h
```
    
**Please note that if You want to store root files/folders permissions You probably want to run the script as root**

<p align="right"><a href="#top">:arrow_up:</a></p>

## Examples

Make a backup of the Documents folder

```console
# python2.7 main.py /Users/jack/Documents/
```
	
Make a backup of the Documents folder with some optional parameters

```console
# python2.7 main.py /Users/jack/Documents/ --out /Users/jack/pRestoreBackups --threads 15
```
	
Restore permissions from a saved backup

```console
# python2.7 main.py /Users/jack/pRestoreBackups/1471187539.67_prestore.list --restore
```

<p align="right"><a href="#top">:arrow_up:</a></p>

## License

This software is licensed under the MIT license that you can find inside the LICENSE.txt file.
Basically You're free to do whatever You want until You credit me for my work.
Every contribution through pull requests on GitHub is very welcome.
Most of our active development is in the master branch, so we prefer to take pull requests there (particularly for new features). 

<p align="right"><a href="#top">:arrow_up:</a></p>
