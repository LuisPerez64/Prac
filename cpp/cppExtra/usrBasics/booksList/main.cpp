#include "booksList.hpp"
#include <map>
int main(int argc, char** argv) {
  // The map object that is used through the whole point.
  std::map<std::string, std::vector<std::string> > fullBookIndex;

  populateFromFile(fullBookIndex);
  populateMap(fullBookIndex);
  populateFile(fullBookIndex);

  return(0);
}


    
