# Barcode Generator


## Description

Thermal printers can have their own set/type of "Programming Language" to generate
labels, barcodes, etc... This projects focus os the [ZPL](https://en.wikipedia.org/wiki/Zebra_(programming_language))
used by Zebra Technologies and theirs products.  
According to Wikipedia it is an "upgrade" to the older `EPL` programming language, check the "Reference" for more details;

### Rationale

This simple script uses the `labelary.com` Web Service to generate labels using the ZPL standard.
As seen on the [documentation](http://labelary.com/service.html#live) you set:

+ Print Density (in dpmm)
+ Label Size (HxW) in inches
+ The actual ZPL code.

Assuming the ZPL is valid the script will output a `.png` file.

### Playground

Test your code at [`labelary`](http://labelary.com/viewer.html) website.

### Usage

#### *nix/Mac:

This script was designed using Python3 - the requirements can be found inside the `.txt` file.

```
$ chmod +x zpl.py
$ zpl.py
```

#### Windows

Make sure Python3 and the requirements are installed. Also make sure Python3 folder 
is set the "Environment Variables".

```
C:>python3 zpl.py
```

### Creating a `.exe` file.

PyInstaller used to be an alternative for cross compiling. Since version >1.5 there's 
no way to cross complie to an `.exe` file (Windows Executable) _inside_ a *nix machine. 
[There's this neat repo that uses a docker image to help you.](https://github.com/cdrx/docker-pyinstaller)


#### TODO

+ Check EPL and other Programming languages
