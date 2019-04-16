#
# Makefile for the calculator program, simple but saves time in cleanup
#

CC = g++
CFLAGS = -Wall 
OBJ = englishToMetricConversion.cpp
LABEL = englishToMetricConverter

all: make clean

make: $(OBJ) 
	$(CC) $(CFLAGS) $< -o$(LABEL)

clean:
	rm *~ *# *.o *.out

cleanExec:
	rm $(LABEL)
