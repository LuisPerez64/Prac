#
# Makefile for basic make procedure, adapted for whatever is needed.
#

CC = g++
CFLAGS = -Wall 
OBJ = vowelOrConsonant.cpp 
LABEL = vowelOrConsonant

all: make clean

make: $(OBJ) 
	$(CC) $(CFLAGS) $< -o$(LABEL)

moveItBack:
	mv $(LABEL) ..

clean:
	rm *~ *# *.o 

cleanExec:
	rm $(LABEL)

makeNewDoc: makeNew startDoc

makeNew:
	mkdir sourceCode documentation && mv Makefile sourceCode 

startDoc:
	cd documentation && emacs -nw "Program Specs.txt" 
