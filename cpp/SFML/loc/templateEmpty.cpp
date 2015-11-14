#include <SFML/Graphics.hpp>

int main(){
 
  sf::RenderWindow window(sf::VideoMode(800, 600),
			  "Empty Window,Set Title in Here!");
 
  window.setKeyRepeatEnabled(false);

  while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event)){
      switch(Event.type){
      case sf::Event::Closed:
	window.close();
	break;
     
      default:
	break;
      }

    }

    window.display();
    window.clear();
  }

  return 0;
}
