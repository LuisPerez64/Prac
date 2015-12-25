#!/bin/bash
#Crontab run process that goes about and checks for   
CSPI='e8:b1:fc:6a:05:09' 

for i in `ifconfig  | grep -P '([0-9|a-f]{2}[:| ]){2,}' -o`; do
    if [ $i == $CSPI ]; then
	cat workLog.txt
	echo date >> ~/bin/workLog.txt
    fi
        
done
