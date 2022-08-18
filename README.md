# pynetcalc
Python Subnet Calculator

## Requirements
Typer

## Install 

1. Git Clone this repo `git clone git@github.com:TyrelCB/pynetcalc.git` or Download Zip and Extract
2. Install Typer `pip3 install "typer[all]"`

## Run
*Make sure your in the pynetcalc directory*

`python netcalc.py --help`

`python netcalc.py netinfo --help`

`python netcalc.py subnet --help`

![help_menus](https://github.com/TyrelCB/pynetcalc/blob/main/help_menus.png)

`python3 netcalc.py netinfo 10.20.30.40/22`

`python3 netcalc.py subnet 10.20.30.40/22 --new-prefix /25`

![example](https://github.com/TyrelCB/pynetcalc/blob/main/examples.png)
