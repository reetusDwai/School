# fx.s
# Read two decimal digits from stdin and interpret that input as an integer between 0 and 99, inclusive
# Compute 27x + 17, where x is the provided integer
# Print the input value, the result in decimal and hexadecimal like this:
# x = 19 : f(x) = 530 or 0x212
# gcc -nostdlib -no-pie fx.s -o fx 
# this line prevents a loader warning
.section .note.GNU-stack,"",@progbits
.section .data
    .comm buffer, 4 # Allocate 4 byte for the result of the function
.section .text
    .global _start
# This program does not use stdlib. The linker recognizes _start
# as the beginning of execution.
_start:
    # Read two characters from stdin
    movq $0, %rax # syscall number for sys_read (0)
    movq $0, %rdi # file descriptor for stdin (0)
    movq $buffer, %rsi # pointer to the buffer
    movq $1, %rdx # number of bytes to read
    syscall

    # Add 1 to the ASCII value of the character
    movb buffer, %al # Load the byte from buffer into AL
    decb %al # Decrement the ASCII value by 1
    movb %al, buffer # Store the result back to buffer

    # compute f(x)


    # Write the modified character to stdout
    movq $1, %rax # syscall number for sys_write (1)
    movq $1, %rdi # file descriptor for stdout (1)
    movq $buffer, %rsi # pointer to the buffer
    movq $1, %rdx # number of bytes to write
    syscall
    # Exit the program
    movq $60, %rax # syscall number for sys_exit (60)
    movq $0, %rdi # status = 0
    syscall
