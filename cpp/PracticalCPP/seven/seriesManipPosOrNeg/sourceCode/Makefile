#
# Makefile for basic make procedure, adapted for whatever is needed.
#

CC = g++ 
CFLAGS = -std=c++11 -g -Wall 
OBJ = seriesManipPosOrNeg.cpp
LABEL = seriesManipPosOrNeg

all: make clean

make: $(OBJ) 
	$(CC) $(CFLAGS) $< -o$(LABEL)

moveItBack:
	mv $(LABEL) ..

clean:
	rm *~ *# *.o 

cleanExec:
	rm $(LABEL)

makeNew:
	mkdir sourceCode documentation && mv Makefile sourceCode
