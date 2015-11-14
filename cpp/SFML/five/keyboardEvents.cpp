#include <SFML/Graphics.hpp>
#include <string>
#include <iostream>

int main(){

  sf::RenderWindow window(sf::VideoMode(800, 600), "Keyboard Events");

  std::string message = "Hello my name is Keilani the Proffessor.\n";
  std::string display = "";

  int index = 0;
  //makes the given window not allow for repeated keys on the presses.
  window.setKeyRepeatEnabled(false);

  while(window.isOpen()){

    sf::Event Event;
    while(window.pollEvent(Event)){
  
      if(Event.type == sf::Event::Closed){
	window.close();
      }
      //Checks if any key is pressed on the keyboard
      if(Event.type == sf::Event::KeyPressed){
	/*
	  Event.key.code stores the identity of the key that was gathered from
	  the previous line. sf::Keyboard::<keyIdentity>
	  can use bitwise operations on the key such as Event.key.control
	  on some of the inherent keys, alt, shift, control... ie.
	  if(Event.key.code == sf::Keyboard::return && Event.key.control)
	  .control returns (0 , 1). This will not work with 
	  Event.key.code == sf::Keyboard::lControl
	*/
	if(Event.key.code == sf::Keyboard::Return){
	  //Implementation of visible code.
	  if(message[index] != '\0'){//Displays the contents of message
	    display += message[index];//character by character.
	    index++;
	  }
	  system("reset");//Sends the clear to the terminal.
	  std::cout << display;//Prints out the value in display.
	}
      
      }
      
    }

    window.display();
  }

  return 0;
}
				    
