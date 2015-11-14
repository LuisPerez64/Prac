#include "booksList.hpp"
// Very comment heavy, first program of its sort I am doing so yeah...

void populateMap(std::map<std::string, std::vector<std::string> >
		 &fullBookIndex) {

  bool speedToggle(false);
  int totalMultiples(0);
  char answer;
  // Adds any duplicate books to the duplicates list. To be used in the prog.
  std::ofstream ofs("Duplicates.txt", std::ofstream::app | std::ofstream::out);
   
  // This is more or less for the point of making things faster when need be.
  std::cout << "Would you like to enact speed toggle? (y/n):";
  std::cin >> answer;
  clearBuffer(); // Make getline work properly...

  if(answer == 'y' || answer == 'Y') {
    speedToggle = true;
    std::cout 
      << "After author name has been input. Begin book name input." 
      << std::endl 
      << "Bypass (y/n) with ~ At Book Name. When finished with said author."
      << std::endl;
  }

  // Heart of the physical input program.
  while(true) {
    std::string name;

    std::cout << "Author's Name: ";
    std::getline (std::cin, name); // Input the authors name into the map.

    if(fullBookIndex.count(name) == 0) {  // Author not in index
      std::vector<std::string> bookIndex; // Wold be redundant, but have to
      fullBookIndex[name] = bookIndex;  // make a new vector for it.
    }
    /*
      Author has been added to the index, if not already found within th map, 
      proceed to add book(s) now, consistently to the map/books list. 
    */
    while(true) {
      std::string book; // New string object for each book to be added.
      std::cout << "Book Name: ";
      std::getline (std::cin, book);
      if(book[0] == '~') // Speed toggle functionality, it's always on.
	break;           
      // Eliminate duplicate books
      
      /*SideNote: Look into why I can use [] and have to use find() for this*/
      /*****************************PseudoCode*******************************
	if (the book is not found already, using the algorithm find function,
	under the authors name indexed vector, then add the book, else, it
	is a duplicate book. Do not add, send to the Duplicates file.
	*********************************************************************/
      if(std::find(fullBookIndex.find(name)->second.begin(),
		   fullBookIndex.find(name)->second.end(),
		   book) == fullBookIndex.find(name)->second.end()) {
	fullBookIndex.find(name)->second.push_back(book);  // Insert the book
	std::cout << "Book Added";
      }else { // Book is a duplicate, do all the things that is needed here.
	totalMultiples++;
	ofs << book << std::endl; // Adds the book to the duplicates list.
	std::cout <<"'" << book << "'"<< " Duplicate!!!"; // Tell the user.
      }
			
      if (!speedToggle){ // The whole y/n seemed tedious, just bullet through
	// and break if the user wants to instead of asking every time.
	/* For speedier functonality Added break above */
	std::cout << std::endl
		  << "Add another book by this author (y / n)?: ";
	std::cin >> answer;
	if (answer == 'n' || answer == 'N')
	  break;

	clearBuffer();
      }
      std::cout << std::endl;
    }
    // Validate that there are(n't) any other authors/books to add.
    std::cout << "Would you like to add another book (By another author)?: ";
    std::cin >> answer;
    if (answer == 'n' || answer == 'N')
      break; // This is the break point, nothing else to do here.
    clearBuffer();
  }
  // Outputs it to the user and also brings it into the needed file.
  if (totalMultiples > 0) {
    std::cout << "Total Duplicates: " << totalMultiples << std::endl;
    ofs <<  "Total Duplicates: " << totalMultiples << std::endl;
  }
  ofs.close();
}

void populateFile(std::map<std::string, std::vector<std::string> >
		  &fullBookIndex) {
  std::ofstream ofs;
  int totalBooks(0);
  
  // Basically opens the file, and makes it a new file in itself.
  ofs.open("Book List.txt", std::ofstream::trunc);
  
  // Creates the iterator to read through the given map. 
  std::map<std::string, std::vector<std::string> >::iterator
    mapIt(fullBookIndex.begin());
  // Iterate through the map, and make things work as they need to.
  for(; mapIt != fullBookIndex.end(); ++mapIt){
    ofs << mapIt->first << ": # of Books " // Input the authors name
	<< mapIt->second.size() << std::endl; // Number of indexed point(books)
    totalBooks+= mapIt->second.size(); // Index for amount of total books
   
    // Sort out the list of books, alphabetical order. algorithm sort
    std::sort(mapIt->second.begin(), mapIt->second.end());

    // Iterator for the vector that is currently being pointed to by mapsIter
    std::vector<std::string>::iterator
      it(mapIt->second.begin());

    // Pushes out all the books held within the vector to the outputFile
    while (it != mapIt->second.end()) {
      ofs << *it;
      ++it;
    }
    ofs << std::endl;
  }
  ofs << std::endl << "Total Number of Books: " << totalBooks;

  ofs.close();
}

/***************************************************************************
 *Stub for now, need regexes for this to work properly, or efficiently...
 *Currently works but is adding new lines that are not needed. SOO CLOSE
 **************************************************************************/
void populateFromFile(std::map<std::string, std::vector<std::string> >
		      &fullBookIndex) {
  std::ifstream inputFile("Book List.txt");
  if(!inputFile.is_open())
    // First iteration. File does not yet exist, return safely
    return;

  std::string inputName, inputLine; // Strings to hold simple data.

  while(inputFile.good()) { // There's a better way to do this...
    std::getline(inputFile, inputLine); //get input from inputFile to inputLine
 
    if(inputLine.find("Total Number of Books:") != std::string::npos) 
      break; // Reached the end of the file itself. Do not add this in...
  
    if(isAuthor(inputLine)) { // New author is being placed in.                
      std::vector<std::string> bookIndex;// New vector made for every author.  
      inputName = authorName(inputLine); // Make function be called once.
      fullBookIndex[inputName] = bookIndex; 
    }else  // Input Line is a book, not an author
      fullBookIndex.find(inputName) -> second.push_back(inputLine);
  }

  inputFile.close();
}


/*************************Helper Functions********************************/
inline void clearBuffer() {
  // This solves the std::getline(std::cin, var) problem, but FUCK ME DAMN!
  while (std::cin.get() != '\n') // Read until a newline is met...
    std::cin.get();
}

bool isAuthor(std::string input) {
  bool isIt(false);

  if(input.find(": #") != std::string::npos)
    isIt = true;

  return(isIt);
}

std::string authorName(std::string input) {
  return(input.substr(0, input.find(':')));
}

 
