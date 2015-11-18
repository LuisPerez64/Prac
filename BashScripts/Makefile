OBJ?= *.c #Generalized grab for the source file, takes in multiples so clean up
cc = gcc -std=c99 #To not complain about the for loop inits
lflags = -lm
flags = -Wall $(lflags) 
exec = test
output = -o $(exec)
editor = emacs -nw #Editor to be used could be changed here to user preference
compileSingle = $(cc) $< $(flags) $(output) #One file compilation
compileMultiple = $(cc) $^ $(flags) $(output) #If multiple files change flag

all: edit make run #Can add clean, but then debugging may be a bit of an issue.

edit: $(OBJ)
	$(editor) $^

make: $(OBJ) #Can switch between single, and multiple here	
	$(compileSingle)

run:
	./$(exec)

clean:
	rm -fr *\~ *\# *.c *.out *.o test  && reset #Clean up procedure
