#!/bin/bash
#Rudimentary format for Finding a file or a directory within the system
echo "Hello, "$USER". Would you like to find a file or a folder?"
printf "(1) File\n(2) Directory \nChoice:" #Echo was complaining

#Search query type collection block
read choice
printf "\n\n"
if [ $choice == 1 ]; then 
    echo -n "Please input the file to locate: "
elif [ $choice == 2 ]; then 
    echo -n "Please input the directory to locate: "
else
    echo "Well that is not one of the options available here. Exiting"
    return 2
fi  
read inputVar
printf "\n"

#Does the user wish search within the given directory, and it's subdirectories
#or go from home directory, and search all the subdirectories within it.
echo -n "Search for "$inputVar" within the current directory? (Y)|(N):"
read searchCurrentDir
while [ $searchCurrentDir != 'y' ] && [ $searchCurrentDir != 'Y' ] &&
[ $searchCurrentDir != 'n' ] && [ $searchCurrentDir != 'Y' ]; do
    echo -n "Please input (Y) or (N): "
    read searchCurrentDir
done

#Capture the directories, in case user wants to CD to it. 
#Will do with files later. Branching on input from above. Search block.
if [ $searchCurrentDir == 'n' ] || [ $searchCurrentDir == 'N' ]; then
    if [ $choice == 1 ]; then
	find ~ -type f -iname $inputVar 2> /dev/null > /tmp/findMe
    else
	find ~ -type d -iname $inputVar 2> /dev/null > /tmp/findMe
    fi 
else 
    if [ $choice == 1 ]; then
	find . -type f -iname $inputVar 2> /dev/null > /tmp/findMe
    else
	find . -type d -iname $inputVar 2> /dev/null > /tmp/findMe
    fi   
fi

#Output manipulation block
cat /tmp/findMe #Three calls to the cat function, there has to be a better way.
contentsOfSearch=`cat /tmp/findMe`
amountOfOccurences=`cat /tmp/findMe | wc -l` #To be used a bit later on.
printf "\n"
if [ $amountOfOccurences == 0 ]; then
    echo "Could not satisfy your query. Exiting"  
    return 3 #If run with source then exit breaks fully
fi
    
#Does the user want to go to the directory they searched for?
goToDir='\0'
if [ $choice == 2 ]; then
    echo "Would you like to cd into the directory?"
    while [ $goToDir != 'y' ] && [ $goToDir != 'Y' ] && 
    [ $goToDir != 'n' ] && [ $goToDir != 'N' ]; do
	echo -n "Please input (y) / (n): " 
	read goToDir
    done
fi

if [ $goToDir == 'y' ] || [ $goToDir == 'Y' ]; then
 #Here to make it so that the user can choose which dir to go to. If wanted,
 #and there are more than one matching sequences within the search.
 if [ $amountOfOccurences != 1 ]; then   
  echo "Are you feeling lucky? Selecting yes will go to the first found dir: "
 feelingLucky='\0'
 while [ $feelingLucky != 'y' ] && [ $feelingLucky != 'Y' ] &&
 [ $feelingLucky != 'n' ] && [ $feelingLucky != 'N' ]; do
     printf "Please input a y/n: "
     read feelingLucky
 done
 else #If only one occurence no need to check for luck.
     feelingLucky='y'
 fi
fi

#CD Can't be execed within the script directly, as changes are done to a temp
#shell enviroment. Run with source or find another manner.
if [ $choice == 2 ]; then 
    if [ $feelingLucky == 'y' ] || [ $feelingLucky == 'Y' ]; then
	cd `cat /tmp/findMe | grep -m 1 $inputVar`
    else
	echo "Going through list of directories attained:"
	cdToThisDir='\0'
	for i in $contentsOfSearch ; do
	    printf "CD to: \n%s\n(Y\\N)?:" $i
	    read cdToThisDir #Error checking is getting tedious.
	    #Turn it into a function, but leave it out for now.
	    if [ $cdToThisDir == 'y' ] || [ $cdToThisDir == 'Y' ]; then
		cd $i
		break
	    fi
	done
    fi
fi
