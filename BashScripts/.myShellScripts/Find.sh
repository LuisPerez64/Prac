#Rudimentary format for Finding a file or a directory within the system
echo "Hello, "$USER". Would you like to find a file or a folder?"
printf  "(1) File\n(2) Directory \nChoice:" #Echo was complaining

read choice
if [ $choice == 1 ]; then 
 echo -n "Please input the file to locate: "
elif [ $choice == 2 ]; then 
 echo -n "Please input the directory to locate: "
else
 echo "Well that is not one of the options available here. Exiting"
 exit 2
fi  
read inputVar

#Verify whether the user wants to search within their current folder or 
#search within their whole home directory for the input point
echo -n "Search for "$inputVar" within the current directory? (Y)|(N):"
read searchCurrentDir
while [ $searchCurrentDir != 'y' ] && [ $searchCurrentDir != 'Y' ] &&
      [ $searchCurrentDir != 'n' ] && [ $searchCurrentDir != 'Y' ]; do
 echo -n "Please input (Y) or (N): "
 read searchCurrentDir
done

#Capture the directories, in case user wants to CD to it. 
#Will do with files later
if [ $searchCurrentDir == 'n' ] || [ $searchCurrentDir == 'N' ]; then
 if [ $choice == 1 ]; then
  find ~ -type f -name $inputVar 2> /dev/null > /tmp/findMe
 else
  find ~ -type d -name $inputVar 2> /dev/null > /tmp/findMe
 fi 
else 
 if [ $choice == 1 ]; then
  find . -type f -name $inputVar 2> /dev/null > /tmp/findMe
 else
  find . -type d -name $inputVar 2> /dev/null > /tmp/findMe
 fi   
fi
cat /tmp/findMe
amountOfOccurences=`cat /tmp/findMe | wc -l` #To be used a bit later on.

#Does the user want to go to the directory they searched for?
goToDir='\0'
if [ $choice == 2 ]; then
 echo "Would you like to cd into the directory (Will go into first result)?"
 while [ $goToDir != 'y' ] && [ $goToDir != 'Y' ] && 
       [ $goToDir != 'n' ] && [ $goToDir != 'N' ]; do
  echo -n "Please input (y) / (n): " 
  read goToDir
 done
fi

#This is not too good of a manner of doing this. Currently goes into the first
#directory with the matching file name, main point is that should there be 
#subdirectories, as in my machine, within .git the first result should be the 
#directory tha holds the .git folder anyways.
if [ $goToDir == 'y' ] || [ $goToDir == 'Y' ]; then
  #CD Can't be execed within the script directly, as changes are done to a temp
  #shell enviroment. Run with source or find another manner.
 cd `cat /tmp/findMe | grep -m 1 $inputVar`
 echo "Should be within the needed directory"
fi
