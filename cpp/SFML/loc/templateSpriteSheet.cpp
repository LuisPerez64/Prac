#include <SFML/Graphics.hpp>
#include <iostream>

int main(){
  sf::RenderWindow window(sf::VideoMode(800, 600),
			  "Sprite Sheet Window, Set Title Here");

  window.setKeyRepeatEnabled(false);

  sf::Texture pTexture;
  sf::Sprite playerImage;

  //Can be renamed to whatever texture being brought in, IntRect Param useable
  if(!pTexture.loadFromFile("Player2.png"))
     std::cout << "Could not load player Image" <<std::endl;

  playerImage.setTexture(pTexture);

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
if(sf::Mouse::isButtonPressed(sf::Mouse::Left))
    std::cout << "X: " << sf::Mouse::getPosition(window).x
              << "Y: " << sf::Mouse::getPosition(window).y <<std::endl;
    window.draw(playerImage);
    window.display();
    window.clear();
  }

  return 0;//Done implicitly, but I like to do it anyways.
}
