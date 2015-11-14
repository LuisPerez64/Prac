//Non commented points are within the hello program in ../one
#include <SFML/Graphics.hpp>

int main(){
  sf::RenderWindow window;
  /*
    Added parameter to the given constructor or renderWindow()
    RenderWindow(modeOfTheWindow(x, y), titleOfWindow, styleOfWindow)
    sf::Style::(Close, Default, Fullscreen, None, Resize, Titlebar)
    Outline these points elsewhere and check different implementations.
    Using a bitwise operation, we are able to add and remove diferent points.
    In this implementation we are able to add a close function to the closeless
    titlebar style code.
    Go into different implementations.
  */

  //The | ~ Or in sf::Style is a bitWise operation.
  //Seems as if adding the style parameter is causing weird things to happen
  //Not bad but pushing everything from the background to the window.
  window.create(sf::VideoMode(800, 600), "My Second SFML Game",
		sf::Style::Titlebar | sf::Style::Close);

  sf::Vector2u size(400, 400);
  /* Would print out the values stored in the 2d Array in size
     std::cout << size.x << " " << size.y << std::endl;
  */
  //Sets the size of the window to the points in the given vector above
  window.setSize(size);
  /*
    Can also be done with this implementation.
    window.setSize(sf::Vector2u (400, 400));
  */
  
  //Changes the title of the given window.  
  window.setTitle("Coding Made Easy");
  
  /*
    Note change from Vector2u to Vector2i for the change in the position
    parameters.
    setPosition() changes the position of the window that is being displayed
    to the user.
  */
  window.setPosition(sf::Vector2i(100, 100));
  
  while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event))
      if(Event.type == sf::Event::Closed)
	window.close();

    window.display();
  }
 
 return 0;
}
