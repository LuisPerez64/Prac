//Needed for the display of window. Functions used below.
#include <SFML/Graphics.hpp>//RenderWindow(Constructor) | VideoMode(x, y) |
                            //Event Manager~ | var.display()

int main(){
  //Video mode display the width and height of the screen. VideoMode
  sf::RenderWindow window(sf::VideoMode(800, 600), "My First SFML Game");
  
  /*
    Or, equivalent points, if the points for window() are not filled in
    the constructor above.
    window.create(sf::VideoMode(800, 600), "My First SFML Game");
  */
  //Runs through as long as the window is not closed
  while(window.isOpen()){
    sf::Event Event; //needed to manage background events, and situations.
  
    //Processing for events that are causing changes to the given interface.
    while(window.pollEvent(Event))
      //If any close events take place for the window then send the signal to
      //close out the window
      if (Event.type == sf::Event::Closed)
	window.close();

    //Displays whatever is stored within the parameters to the opened window 
    window.clear();
    window.display();

  }

  return 0;
}
