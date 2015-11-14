#include <SFML/Graphics.hpp>
#include <iostream>
/*
Vectors~
        2i ~ Ints
	2u ~Unsigned Ints
	2f ~floats
*/

int main(){
  float min = 0, max = 0;
  int toggle = 0;

  sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Time",
			  sf::Style::Titlebar | sf::Style::Close);
  sf::Clock clock;

  sf::Time time3;
  //sf::seconds | microseconds | miliseconds (set time)
  sf::Time time  = sf::seconds(2);
 
  //Can do algebraic operations on the times as well.
  time += sf::milliseconds(2000);
  
  //To display .( asSeconds() || asMiliseconds() || asMicroSeconds())
  std::cout << time.asMilliseconds() << std::endl;

  //Resize, retitle, orientate. heed 2i, 2u convention changes
  window.setSize(sf::Vector2u(400, 400));
  window.setTitle("Still SFML Time");
  window.setPosition(sf::Vector2i(100, 100));

  while(window.isOpen()){
    
    sf::Event Event;
    while(window.pollEvent(Event))
      if(Event.type == sf::Event::Closed)
	window.close();
    
    //Sets the time as the point of the time that has elapsed.
    time3 = clock.getElapsedTime();
    
    //Prints out the time that has elapsed since the last restart
    std::cout << "Time: " << time3.asSeconds() <<std::endl;
    
    {//Measures the time between instances, gets the slowest and fastest time 
      //needed for a cycle.

      if(toggle < 10){//Lets the program cycle through few times before
	              //assigning to get concise data.
	max =  min = time3.asSeconds();
	toggle +=1;
      }

      if(time3.asSeconds() <= min)
	min = time3.asSeconds();
      if(time3.asSeconds() >= max)
	max = time3.asSeconds(); 
    }

    //Resets the clock and also returns the elapsed time to the user.
    clock.restart();

    window.display();
  }

  //Prints out the needed points that are set.
  // std::cout << "Min: " << min << " Max: " << max <<std::endl;
  return 0;
}
