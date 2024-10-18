# pred_nsl.s
# Read one character from stdio, decrement one to the ASCII value, and write
# it on stdout.
# gcc -nostdlib -no-pie pred_nsl.s -o pred_nsl 
# this line prevents a loader warning
.section .note.GNU-stack,"",@progbits
.section .data
    .comm buffer, 1 # Allocate 1 byte for the input character
.section .text
    .global _start
# This program does not use stdlib. The linker recognizes _start
# as the beginning of execution.
_start:
    # Read a single character from stdin
    movq $0, %rax # syscall number for sys_read (0)
    movq $0, %rdi # file descriptor for stdin (0)
    movq $buffer, %rsi # pointer to the buffer
    movq $1, %rdx # number of bytes to read
    syscall

    # Add 1 to the ASCII value of the character
    movb buffer, %al # Load the byte from buffer into AL
    decb %al # Decrement the ASCII value by 1
    movb %al, buffer # Store the result back to buffer

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
