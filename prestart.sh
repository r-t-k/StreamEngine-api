#!/bin/bash

#restart this script as root, if not already root
[ `whoami` = root ] || exec sudo $0 $*



pip install -r requirements.txt
