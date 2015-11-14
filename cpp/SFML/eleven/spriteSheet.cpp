#include <SFML/Graphics.hpp>
#include <iostream>
#include <string>

int main(){
  enum Direction {Down, Left, Right, Up};
  //lets us know where to start drawing from 
  sf::Vector2i source(1, Down);
  //accesable with source.x , source.y / Mut source.x = var ...
  int x = 0,y = 0;
  sf::RenderWindow window(sf::VideoMode(800, 600), "ANIMATION!!!!");

  //  window.setKeyRepeatEnabled(false);

  sf::Texture pTexture;
  sf::Sprite playerImage;
  //Error Check
  if(!pTexture.loadFromFile("Player.png")){
    std::cout << "Error. Could not load in Image." << std::endl;
    return 1;
  }

  playerImage.setTexture(pTexture);

  while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event)){
      switch(Event.type){
      case sf::Event::Closed:
	window.close();
	break;
	/*
	  The next block of code is an implementation of the movement through
	  the sprite sheet that was handed to the texture object.
	  It's easily implemented, attempting to explain it to myself at the
	  moment. The source.y will hold the value of the starting Y location,
	  of the IntRect function. The enumerated values,0 - 3, will outline
	  which value, *32 for the sprite pack, will be the starting Y-Axis
	  at 2*32, and so forth.
	  setPosition updates the location of the image to simulate movement.
	  Not a smooth movement as of yet. Will implement this in a better 
	  manner later on.
	  There is a serious lag in the event procession.
	 */
      case sf::Event::KeyPressed:
	switch(Event.key.code){
	case sf::Keyboard::Up:
	  source.y = Up;
	  y-=5;

	  break;
	case sf::Keyboard::Down:
	  source.y = Down;
	  y+=5;

	  break;
	case sf::Keyboard::Left:
	  source.y = Left;
	  x-=5;

	  break;
	case sf::Keyboard::Right:
	  source.y = Right;
	  x+=5;

	  break;
	default:
	  break;
	}

      default:
	break;
      }
    }
    playerImage.setPosition(x,y);
    /*
      The source.x value holds the value for the starting X-Axis position
      from the input texture. Multiplying it by 32 moves down the sprite pack
      that is being brought in, and then cycles through them, as long as it 
      does not exceed the bounds of the texture that is being brought in.
    
      this will cause the image to basically move to the leftcycling until max
      X length is found, and starting over. Causing the illusion of movement.
    */
    source.x++;//Causes the image to loop along the given axis.
    if(source.x * 32 >= (signed int) pTexture.getSize().x)//Move to the next 
      source.x = 0;//Resets to the top of the cycle point.

    /*
      This is where the texture that is being printed out is updated, and moved
      through with the values that had been changed in the prior loops.
      multiplying the values in source, ranging from 0-3 multiplied by 32, to 
      accomodate the 32x32 size of the sprite to be printed.
    */
    playerImage.setTextureRect(sf::IntRect(source.x *32, source.y*32, 32, 32));
					     
    window.draw(playerImage);
    window.display();
    window.clear();
  }

  return 0;
}				 
