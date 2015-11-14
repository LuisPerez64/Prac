#
# Makefile program given in Label
#

CC = g++
CFLAGS = -Wall
OBJ = serialTransmissionLine.cpp
LABEL = serialTransmissionLineTimeCalculator

all: make clean

make: $(OBJ)
	$(CC) $(CFLAGS) $< -o$(LABEL)

clean:
	rm *~ *# *.o

cleanExec:
	rm $(LABEL)
