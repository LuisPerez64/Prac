CC = g++
CFLAGS = -Wall -Werror -pedantic -ansi

all: make clean

make: hello.cpp
	$(CC) $< $(CFLAGS) -ohello

clean:
	rm *~ *# *.o
