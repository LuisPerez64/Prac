#!/bin/bash
#Set up the internal points within each of the directories,
#used for each of the folders in the given directory creating the 
#needed points in each of them.
 
for i in `find . -type d`; do 
    if [ `pwd $i` != $PWD ]; then #Done to not create files in header folder.
	mkdir $i/sorts $i/implementationNotes $i/headers $i/source;
    fi;
done;
