#
# Makefile for basic make procedure, adapted for whatever is needed.
#

CC = g++
CFLAGS = -Wall 
OBJ = salesTaxCalculator.cpp
LABEL = salesTaxCalculator

all: make clean

make: $(OBJ) 
	$(CC) $(CFLAGS) $< -o$(LABEL)

moveItBack:
	mv $(LABEL) ..

clean:
	rm *~ *# *.o 

cleanExec:
	rm $(LABEL)
