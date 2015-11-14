#include <SFML/Graphics.hpp>
#include <iostream>

int main(){

  sf::RenderWindow Window(sf::VideoMode(400, 400), "Mouse Events");


  while(Window.isOpen()){
    sf::Event Event;

    while(Window.pollEvent(Event)){
      switch(Event.type)
	{
	case sf::Event::Closed:
	  Window.close();
	  break;
	case sf::Event::MouseEntered://Activates when mouse enters the window
	  std::cout << "Mouse within screen bounds." <<std::endl;
	  break;
	case sf::Event::MouseLeft://Activates when the mouse exits the window.
	  std::cout <<"Mouse Not Within the screen bounds." <<std::endl;
	  break;
	case sf::Event::MouseMoved://If the mopuse has moved within the window.
	  //mouseMove.(x || y) maps out the x and y variables of the mouse
	  //within the window.
	  std::cout << "X: " << Event.mouseMove.x << "Y: " << Event.mouseMove.y
		    << std::endl;
	  break;
	case sf::Event::MouseButtonPressed://Activates if a button is pressed.
	  /*
	    mouseButton. (x || Y) relays the position at which the mouse
	    had been clicked within the given window.
	  */
	  if(Event.mouseButton.button == sf::Mouse::Left)//Left pressed
	    std::cout<< "Left Button Pressed at X: " << Event.mouseButton.x
		     << " Y: " <<Event.mouseButton.y <<std::endl;
	  if(Event.mouseButton.button == sf::Mouse::Right)//Right Pressed
	    std::cout<< "Right Button Pressed at X: " << Event.mouseButton.x
		     << " Y: " <<Event.mouseButton.y <<std::endl;
	  break;
	case sf::Event::MouseWheelMoved://Checks if the user has scrolled 
	  //Delta is the net change in position after scrolling.
	  std::cout << "Delta: " << Event.mouseWheel.delta <<std::endl;
	default:
	  break;
	}
    }
    Window.display();
  }

  return 0;
}
