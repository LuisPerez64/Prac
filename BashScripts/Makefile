OBJ?= *.c #Generalized grab for the source file, takes in multiples so clean up
CC = gcc -std=c99 #To not complain about the for loop inits
LFLAGS = -lm -g
WFLAGS = -Wall  
EXEC = test
OUTPUT = -o $(EXEC)
EDITOR = emacs -nw #Editor to be used could be changed here to user preference
COMPILESINGLE = $(CC) $< $(WFLAGS) $(LFLAGS) $(OUTPUT) #One file compilation
COMPILEMULTIPLE = $(CC) $^ $(WFLAGS) $(LFLAGS) $(OUTPUT) #If multiple files change flag

all: edit make run #Can add clean, but then debugging may be a bit of an issue.

edit: $(OBJ)
	$(EDITOR) $^
	cp quiz1.txt quiz.txt
make: $(OBJ) #Can switch between single, and multiple here	
	$(COMPILESINGLE)

run:
	./$(EXEC) 
	grep 'close' *.c 
#	cat output.txt
	cat average.txt quiz.txt
#	grep -E -e '5' -e '10.5' -e '79.07' -e '190' -e '9' -e '86' -e '438' output.txt -o >grepOut.txt #Output for 
#	diff grepOut.txt grepO.txt
clean:
	rm -fr *\~ *\# *.c *.out *.o test output.txt && reset #Clean up procedure
