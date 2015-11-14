#include <SFML/Graphics.hpp>
#include <iostream>
#include <string>

int main(){

  sf::RenderWindow window(sf::VideoMode(800,600), " Text Events");
  std::string display ="";
  window.setKeyRepeatEnabled(false);

  while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event)){
      
      switch(Event.type){

      case sf::Event::Closed:
	window.close();
	break;

	//Different from KeyPressed, allows the input of special chars by dflt.
      case sf::Event::TextEntered:
	if(Event.text.unicode != 8)//Returns the ascii vlaue of the key pressed
	  display += (char)Event.text.unicode;//Cast ascii to char store in str
	else//Case for handling the space being pressed, allows for spaces
	  display = display.substr(0, display.length() -1);

	system("reset");	    
	std::cout << display;

	break;

      default:
	break;
      }
    }

    window.display();
  }

  std::cout << std::endl;
  return 0;
}
