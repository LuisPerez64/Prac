#
# Makefile for the calculator program, simple but saves time in cleanup
#

CC = g++
CFLAGS = -Wall 
OBJ = dateArithmeticCalculator.cpp
LABEL = dateArithmeticCalculator

all: make clean

make: $(OBJ) 
	$(CC) $(CFLAGS) $< -o$(LABEL)

clean:
	rm *~ *# *.o 

cleanExec:
	rm $(LABEL)
