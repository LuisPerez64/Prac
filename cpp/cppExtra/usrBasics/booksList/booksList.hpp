#ifndef BOOK_LIST_HPP
#define BOOK_LIST_HPP

#include <algorithm> // std::find | std::sort                                  
#include <map> // std::map<index, data>                                        
#include <vector> // std::vector<data>                                         
#include <string> // std::string                                               
#include <iostream> // std::cout | std::cin | std::getline                     
#include <fstream> // std::ifstream | std::ofstream 
/*
  Implementing first hand a map data structure that is holding its index value 
  by authors names, if the authors name is found then add books under that
  author, if the book is found under that author already then display message 
  "This is a duplicate" then act accordingly due to that information. 
  Maps are a vital data structure try hard to do this with as little online
  help as possible.
*/
/*
  Milestones:
~~    One: Implement the map of book titles by author
~~    Two: Port that map out, in an orderly fashion to a file
    Three: Instantiate a way to read from that file, if it's not empty,
       or exists. If it does exist then read in from the file and populate the
       map data structure using it, maybe using regex? 
    Four: Add in the ability to go through the list, and state wheter you have
       read the books or Not. Can be implemented with the search feature as 
       well. Help keep things in order.

    Extra points:
~~     Milestone One: Put the list in by alphabetical order, based on author, 
          and then book title within the author
~~     Milestone Two: Make that point from One, and it should transfer alpha
          order
      Milestone Null:
        Add in SFML Functionality, yeah this may be unneeded, but I want to.
        Add search feature
	Add number of books by author to the outputFile
	Overall Books Number at the Title point, beginning of file
	Ability to seperate Books into multiple files, while still making a 
	  mass library, but the user can specify a genre and so on.

~~Done~~
   Visual Points Wanted output for outputFile
     Author's Name: # Of Books By Author
       Books List in Alphabetical Order    
*/

/*
  Pre : Is Called
  Post: Returns the map filled.
*/
void populateMap(std::map<std::string, std::vector<std::string> >
		 &fullBookIndex);

/* 
   Pre : File to be output to already exists.
   Post: Returns a filled map, populated from the initial input file.
     Discards the file? May not need to do this though.
*/
void populateFromFile(std::map<std::string, std::vector<std::string> >
		      &fullBookIndex);
/*
  Pre: Is Called
  Post: The output file is updated, with the added books
*/
void populateFile(std::map<std::string, std::vector<std::string> >
		 &fullBookIndex);

/*
  Pre : Is Called
  Post: Cleans the buffer. Eliminates problems with getline.
*/
inline void clearBuffer();

/*
  Pre: Is Called
  Post: If a specific string is met, and matched then an author has been found.
*/
bool isAuthor(std::string);

/*
  Pre: Is Called
  Post: Returns the substr that holds the authors name ot the caller.
*/
std::string authorName(std::string);

#endif  //BOOK_LIST_HPP
