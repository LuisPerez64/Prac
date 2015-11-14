#include <SFML/Graphics.hpp>
#include <iostream>


int main(){
  enum Direction {Down, Left, Right, Up};
  int toggle = 1;
  sf::Vector2i source(1, Down);
  sf::RenderWindow window(sf::VideoMode(800, 600), "Keyboard Input In Depth",
			  sf::Style::Titlebar | sf::Style::Close);
  float frameCounter=0, switchFrame = 100, frameSpeed = 500; 
 
  window.setKeyRepeatEnabled(false);

  sf::Texture pTexture;
  sf::Sprite playerImage;
  sf::Clock clock;

  if(!pTexture.loadFromFile("Player.png"))
    std::cout << "Image file not found." << std::endl;

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

    //Static implementation, isKeyPressed() checks if any key at all is pressed
    //Causes a faster reaction from the program than the Event.key.code does.
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Up)){
      toggle = 1;//Shows that there has been a change in directions
      source.y = Up;
      playerImage.move(0, -1);//Moves the sprite, by the point given, by pixel.
    }else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Down)){
      toggle = 1;
      source.y = Down;
      playerImage.move(0, 1);
    }else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Right)){
      toggle = 1;
      source.y = Right;
      playerImage.move(1, 0);
    }else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Left)){
      toggle = 1;
      source.y = Left;
      playerImage.move(-1, 0);
    }
    //Go over this in depth. Bring in as sample code to dir.txt
    //This is meant to make it so that the screen refreshes at a constant rate
    //accorss platforms and hardware implementatations.
    frameCounter+= frameSpeed * clock.restart().asSeconds();
    if(frameCounter >= switchFrame){     
      source.x++;
      if(source.x * 32 >= (signed int)pTexture.getSize().x)
	source.x = 0;
      frameCounter = 0;
    }

    if(toggle){//Makes it look as if the user isnt moving if no button pressed.
      playerImage.setTextureRect(sf::IntRect(source.x *32,source.y *32,32,32));
      toggle = 0;//Reset the toggle after movement, stops unneded animation.
    }

    window.draw(playerImage);
    window.display();
    window.clear();
  }

  return 0;
}
