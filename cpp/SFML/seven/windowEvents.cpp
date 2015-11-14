#include <SFML/Graphics.hpp>
#include <iostream>

int main(){
  sf::RenderWindow window;
  window.create(sf::VideoMode(800, 600), "Window Events");

  while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event)){
      /*Working with Multiple possible events using a switch
	if(Event.type == sf::Event::Closed)
	window.close();
	Rehashed code that has been used so far to keep it fresh.
      */
      switch(Event.type){
      case sf::Event::Closed:
	window.close();
	break;
	/*
	  Points that monitor wheter or not the given window is the one that
	  will attain the igiven commands.
	  Activated if the user clicks inside or outside of the game window.
	*/
      case sf::Event::GainedFocus:
	std::cout << "Window active" <<std::endl;
	break;
      case sf::Event::LostFocus:
	std::cout << "Window not active" << std::endl;
	break;

	/*
	  Returns with the parameters width and height the rescaled size
	  of the active window. activated if any resize operation is done.
	*/
      case::sf::Event::Resized:
	std::cout << "Window Resized to (" << Event.size.width << ", "
		  << Event.size.height <<std::endl;
	break;


      case sf::Event::KeyPressed:
	if(Event.key.code == sf::Keyboard::Return)
	  std::cout << "Enter Pressed." <<std::endl;
	break;

      case sf::Event::MouseButtonPressed:
	if(Event.mouseButton.button == sf::Mouse::Left)
	  std::cout << "Left Mouse Button Pressed" <<std::endl;
	break;

      case sf::Event::MouseMoved:
	std::cout << "X: " << Event.mouseMove.x 
		  << "Y: " << Event.mouseMove.y <<std::endl;
	break;

      default:
	break;
      }
    }

    window.display();
  }

  return 0;
}
