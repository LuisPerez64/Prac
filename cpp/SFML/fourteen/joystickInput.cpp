#include <SFML/Graphics.hpp>
#include <iostream>
//sf::Joystick::update() Updates points to the joystick itself.
int main(){
  enum Direction{Down, Left, Right, Up};
  sf::Vector2i source(1, Down);//Starting position. (1, 0);

  sf::RenderWindow window(sf::VideoMode(800, 600), 
			  "Joystick Input!");

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

  if(sf::Joystick::isConnected(0))
    std::cout << "Joystick 1 is Connected" <<std::endl;
  else
    std::cout << "Joystick 1 is not Connected" << std::endl;
  /*
    int buttonCount = sf::Joystick::getButtonCount(0);
    std::cout << buttonCount <<std::endl;
  Checks if one of the axises exists on the given keyboard, dont know what Z is
  though.
  bool hasAxis = sf::Joystick::hasAxis(0, sf::Joystick::Z);
  */
  while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event)){
      switch(Event.type){
      case sf::Event::Closed:
	window.close();
	break;
	/*
	  case sf::Event::JoystickButtonPressed:
	  std::cout << "Button: " << Event.joystickButton.button <<std::endl;
	  break; 
	*/
      default:
	break;
      }

    }

    if(sf::Joystick::isButtonPressed(0, 12))
      updateFrame = true;
    else if(sf::Joystick::isButtonPressed(0, 13))
      updateFrame = false;

    sf::Vector2f moveSpeed(sf::Joystick::getAxisPosition(0, sf::Joystick::X),
			   sf::Joystick::getAxisPosition(0, sf::Joystick::Y));

    if(moveSpeed.x > 0)
      source.y = Right;
    else if(moveSpeed.x < 0)
      source.y = Left;
    else if(moveSpeed.y > 0)
      source.y = Down;
    else if(moveSpeed.y < 0)
      source.y = Up;
    //Explain this point in dir.txt
    playerImage.move(moveSpeed.x * clock.getElapsedTime().asSeconds(),
		     moveSpeed.y * clock.getElapsedTime().asSeconds());
    //Static implementation of the movement using keyboard | joystick.
    if(updateFrame){
      //study this loop.
      frameCounter += frameSpeed * clock.restart().asSeconds();
      if(frameCounter>= switchFrame){
	source.x++;
	if(source.x *32 >= (signed int) pTexture.getSize().x)
	  source.x = 0;
	frameCounter = 0;
      }
    }
    //Refresh the image.
    playerImage.setTextureRect(sf::IntRect(source.x*32, source.y*32, 32, 32));

    window.draw(playerImage);
    window.display();
    window.clear();
  }

  return 0;//Done implicitly, but I like to do it anyways.
}
