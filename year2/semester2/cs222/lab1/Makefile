# Compiler and flags
CC = gcc
CFLAGS = -Wall -g

# Default target: Builds both programs
all: bart bwrite

# Rule to create bart from bart.c
bart: bart.o
	$(CC) bart.o -o bart

# Rule to create bwrite from bwrite.c
bwrite: bwrite.o
	$(CC) bwrite.o -o bwrite

# Rule to compile bart.c to bart.o
bart.o: bart.c
	$(CC) $(CFLAGS) -c bart.c

# Rule to compile bwrite.c to bwrite.o
bwrite.o: bwrite.c bwrite.h
	$(CC) $(CFLAGS) -c bwrite.c

# Clean-up target
clean:
	rm -f *.o bart bwrite

# Man page formatting and installation
man: bart.man
	nroff -man bart.man > bart.1

# Rule to install the man page
install_man: bart.1
	install -m 644 bart.1 /usr/share/man/man1

# Clean the formatted man page
clean_man:
	rm -f bart.1

# Target to zip all files into k_smith_lab3.zip
zip: bart.c bart.man bwrite.c bwrite.h Makefile
	zip k_smith_lab3.zip bart.c bart.man bwrite.c bwrite.h Makefile
