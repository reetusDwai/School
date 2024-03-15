prog2:main.o stack.o
	gcc -o prog2 main.o stack.o
	make clean
stack.o:stack.c
	gcc -c stack.c
main.o:main.c
	gcc -c main.c

clean:
	rm main.o stack.o prog1
