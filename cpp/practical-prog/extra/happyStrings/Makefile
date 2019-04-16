OBJ= happyStrings.o 
CC= g++
CFLAGS= -Wall -pedantic -ansi -g 

all:happyStrings clean

happyStrings:happyStrings.o
	$(CC) $(OBJ) $(CFLAGS)

happyStrings.o: happyStringsCons.o happyStringsMain.o
	$(CC) -c $< $(CFLAGS)  

happyStringsCons.o:happyStringsCons.cpp happyStrings.hpp
	$(CC) -c $< $(CFLAGS)

happyStringsMain.o:happyStringsMain.cpp happyStrings.hpp
	$(CC) -c $< $(CFLAGS)

clean:
	/rm *.o *# *.gch
