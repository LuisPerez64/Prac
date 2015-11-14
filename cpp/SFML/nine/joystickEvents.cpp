#include <SFML/Graphics.hpp>
#include <iostream>

int main(){
  sf::RenderWindow window(sf::VideoMode(800,600), "Joysticks!");
  
  window.setKeyRepeatEnabled(false);
       

  while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event)){
      
      switch(Event.type){
      
      case sf::Event::Closed:
	window.close();
	break;

	/*
	 *Joystick IDs act as arrays. If joystickConnect.joystickId is not 
	 *incremented by one it would return as player 0.
	 */
      case sf::Event::JoystickConnected:
	std::cout << "Joystick " <<Event.joystickConnect.joystickId +1 
		  << " is connected" << std::endl;
	break;
      case sf::Event::JoystickDisconnected:
	std::cout << "Joystick: " << Event.joystickConnect.joystickId +1
		  << " is Disconnected" << std::endl;
	break;

      case sf::Event::JoystickButtonPressed:
       	std::cout << "Button: :" << Event.joystickButton.button <<std::endl;
	//attack = Event.joystickButton.button;//Sets attack to the button 
	break;
	//Look into wasy to manage both joysticks not just left.
      case sf::Event::JoystickMoved:
	std::cout << "Axis: "<< Event.joystickMove.axis <<std::endl;
	if(Event.joystickMove.axis == sf::Joystick::X)
	  std::cout << "X~Axis: " << Event.joystickMove.position
		    <<std::endl; 
	if(Event.joystickMove.axis == sf::Joystick::Y)
	  std::cout << "Y~Axis: " << Event.joystickMove.position
		    <<std::endl; 
	break;
	
      default:
	break;
      }
    }
    
    window.display();
  }

  return 0;
}
