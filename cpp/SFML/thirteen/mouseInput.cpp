#include <SFML/Graphics.hpp>
#include <iostream>
/*
 Global variable for directions, to be used with multiple points of code,
 better to make it easily accessible.
*/
enum Direction{Down, Left, Right, Up};

int main(){

  sf::Vector2i source(1, Down);//Starting position.

  sf::RenderWindow window(sf::VideoMode(800, 600), 
			  "Mouse Input");

  window.setKeyRepeatEnabled(false);
  sf::Clock clock;//To be used for the frameRate reproduction.
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
    
    //Follows the mouse as long as the left mouse button is pressed down.
    if(sf::Mouse::isButtonPressed(sf::Mouse::Left)){
      sf::Vector2i Position = sf::Mouse::getPosition(window);
      if(playerImage.getPosition().x > Position.x){
	source.y = Left;
	playerImage.move(-1, 0);
      }else if(playerImage.getPosition().x < Position.x){
	source.y = Right;
	playerImage.move(1, 0);
      }else if(playerImage.getPosition().y >Position.y){
	source.y = Up;
	playerImage.move(0, -1);
      }else if(playerImage.getPosition().y < Position.y){
	source.y = Down;
	playerImage.move(0, 1);
      }
    }

    // Keypress dominated movement as well.
    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Up)){
      source.y = Up;
      playerImage.move(0, -1);
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
    
    /*
      If window is not set as the the param, the global window scope's relayed 
      This causes the mouse positon vector to capture the location of the mouse
      relateable to the MouseMoved Event, but is static.

      sf::Vector2i mousePosition = sf::Mouse::getPosition(window);
      std::cout << "X: " << mousePosition.x 
      << " Y: "<< mousePosition.y <<std::endl;  
    */    

    /*
      Moves the move to the given position. If window is not set as a parameter
      then moves to 100, 100 on the global scope, as in the full window.
      sf::Mouse::setPosition(sf::Vector2i(100,100), window);    
    */
 
    //Simple Boolean if-Else statement with ?, need to practice that 
    frameCounter = (updateFrame) ?
      frameCounter + frameSpeed* clock.restart().asSeconds() :
      0;
  
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
