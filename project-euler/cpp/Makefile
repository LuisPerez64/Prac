obj?=holder.cpp #Renameable, mutable for all files
output?=holder #" ^^ "
CC= g++ #Not using the newest standard as of yet, but will soon
CFLAGS = -Wall -Werror #No warnings, treat them as errors
LFLAGS = -lm
EDITOR = emacs -nw

#If avoids overwriting the input with the output by mistake within compilation.
all: isValid? #Only runs the needed command points if the output != obj
ifeq ($(obj), $(output))
isValid?: #Produce an error to the user in this case
	echo "Same name for both input, and output objects\n"
else #Run the makefile as is needed from here on out.
isValid?:review make test clean
endif

review: $(obj)
	$(EDITOR) $^

make: $(obj)
	$(CC) $^ $(CFLAGS) $(LFLAGS) -o $(output);	

test:$(output)
	time ./$(output)
clean:
	rm -f *\# *\~ *.out *.o
