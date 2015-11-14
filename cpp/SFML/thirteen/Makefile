OBJ = 	mouseInput.cpp
CC = g++
CFLAGS = -Wall -Werror
LFLAGS = -lsfml-window -lsfml-system -lsfml-graphics

all: make clean

make: mouseInput.o
	$(CC) $< $(CFLAGS) $(LFLAGS) -o SFMLHello

mouseInput.o: $(OBJ)
	$(CC) $< $(CFLAGS) -c $(LFLAGS)

clean: 
	rm *.o *.out *~ *#
