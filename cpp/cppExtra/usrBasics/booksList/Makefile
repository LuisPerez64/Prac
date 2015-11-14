CC=g++
CFLAGS= -Wall 

all: make clean

make: main.o populate.o
	$(CC) $^ $(CFLAGS) -obookRecordKeep

main.o: main.cpp
	$(CC) -c $< 

populate.o: populate.cpp
	$(CC) -c $< 

clean:
	rm *~ *# *.o
