OBJ?= *.c #Generalized grab for the source file, takes in multiples so clean up
CC = gcc -std=c99 #To not complain about the for loop inits
LFLAGS = -lm
WFLAGS = -Wall  
EXEC = test
OUTPUT = -o $(EXEC)
EDITOR = emacs -nw #Editor to be used could be changed here to user preference
COMPILESINGLE = $(CC) $< $(FLAGS) $(OUTPUT) #One file compilation
COMPILEMULTIPLE = $(CC) $^ $(FLAGS) $(OUTPUT) #If multiple files change flag

all: edit make run #Can add clean, but then debugging may be a bit of an issue.

edit: $(OBJ)
	$(EDITOR) $^

make: $(OBJ) #Can switch between single, and multiple here	
	$(COMPILESINGLE)

run:
	./$(EXEC)

clean:
	rm -fr *\~ *\# *.c *.out *.o test  && reset #Clean up procedure
