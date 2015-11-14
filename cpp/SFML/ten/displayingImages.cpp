#include <SFML/Graphics.hpp>
#include <iostream>
#include <string>
#include <cstdlib>

int main(){

  sf::RenderWindow window (sf::VideoMode (800, 600), "Displaying Images!");

  window.setKeyRepeatEnabled(false);
  int x ,y;
  x = y =0;
  sf::Texture pTexture;
  sf::Sprite playerImage;
  //(Starting pos x,y) , width,height
  if(!pTexture.loadFromFile("Player.png", sf::IntRect(32,0, 32, 32)))
    std::cout << "Error. Could not load player image." <<std::endl;
  playerImage.setTexture(pTexture);
  playerImage.setPosition(400, 300);


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
    x = rand() % 800;
    y = rand() % 600;
    playerImage.setPosition(x, y);
    window.draw(playerImage);
    window.display();
    window.clear();
  }

  return 0;
}
