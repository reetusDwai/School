main_output: main.o queue.o
	gcc -o main_output main.o queue.o
	make clean
main.o: main.c
	gcc -c main.c
queue.o: queue.c
	gcc -c queue.c
clean:
	rm main.o queue.o
