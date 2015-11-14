#include <SFML/Graphics.hpp>
#include <iostream>

int main(){
  enum Direction{Down, Left, Right, Up};
  sf::Vector2i source(1, Down);//Starting position. (1, 0);

  sf::RenderWindow window(sf::VideoMode(800, 600), 
			  "Sprite Sheet Window, Set Title Here");

  //To be used for the frameRate stabilization.
  window.setKeyRepeatEnabled(false);
  sf::Clock clock;
  float frameCounter = 0, frameSpeed = 500, switchFrame = 100;
  bool updateFrame = true;

  sf::Texture pTexture;
  sf::Sprite playerImage;

  //Can be renamed to whatever texture being brought in, IntRect Param useable
  if(!pTexture.loadFromFile("Player.png"))
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

    //Static implementation of the movement using keyboard keys.
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Up)){
      source.y = Up;
      playerImage.move(0, -1);//Increment the relayed (x, y) positions.
    }else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Down)){
      source.y = Down;
      playerImage.move(0, 1);
    }else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Right)){
      source.y = Right;
      playerImage.move(1, 0);
    }else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Left)){
      source.y = Left;
      playerImage.move(-1, 0);
    }

    //Study this loop.
    frameCounter += frameSpeed * clock.restart().asSeconds();
    if(frameCounter>= switchFrame){
      source.x++;
      if(source.x *32 >= (signed int) pTexture.getSize().x)
	source.x = 0;
      frameCounter = 0;
    }
    //Refresh the image.
    playerImage.setTextureRect(sf::IntRect(source.x*32, source.y*32, 32, 32));

    window.draw(playerImage);
    window.display();
    window.clear();
  }

  return 0;//Done implicitly, but I like to do it anyways.
}
