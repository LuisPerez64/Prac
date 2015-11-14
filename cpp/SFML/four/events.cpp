#include <SFML/Graphics.hpp>
#include <iostream>

int main(){

  sf::RenderWindow window(sf::VideoMode(800, 600), "Events Tutorial");
  // sf::Style::Titlebar | sf::Style::Close);

  std::cout << "Press a key To Continue" <<std::endl;

  while(window.isOpen()){
      
    sf::Event Event;
    while(window.pollEvent(Event))
      if(Event.type == sf::Event::Closed)
	window.close();

    /*
      Waits until a specific event is triggered, before allowing the program
      to run forward and do whatever else is needed.
    */
    if(window.waitEvent(Event))
      std::cout << "Event Processed";  
    
    window.display();
  }

  return 0;
}
