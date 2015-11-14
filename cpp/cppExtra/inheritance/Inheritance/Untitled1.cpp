#include <SFML/Graphics.hpp>
#include <iostream>

int main(){
sf::ConvexShape polygon;
sf::RenderWindow window(sf::VideoMode(400, 400), "EL TITULO");

polygon.setPointCount(3);
polygon.setPoint(0, sf::Vector2f(100,100));
polygon.setPoint(1, sf::Vector2f(100, 200));
polygon.setPoint(2, sf::Vector2f(200, 100));
polygon.setOutlineColor(sf::Color::Red);
polygon.setOutlineThickness(5);
polygon.setPosition (200, 200);

while(window.isOpen()){
    sf::Event Event;

    while(window.pollEvent(Event)){
        if(Event.type == sf::Event::Closed)
            window.close();
        }
     window.draw(polygon);
     window.display();
     window.clear();
}
}
