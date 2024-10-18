# Prompt

# Using ATT assembly write the following

# write an assembly program that inputs a single
# character from stdin and then prints the character before it to stdout. For example, if you enter a ’D’,
# your program will output a ’C’. In order for your character to be passed to your program, you will
# have to press the enter key to flush the input buffer. Your program will output only one character.

# The char_in buffer is weird and it is calling the kernal instead of syscall

.section .bss
char_in:    .skip 1         # Reserve 1 byte for the input character

.section .text
.global _start

_start:
    # Read a single character from stdin (file descriptor 0)
    movl $0, %eax          # syscall number for sys_read (0)
    movl $0, %ebx          # file descriptor 0 (stdin)
    movl $char_in, %ecx    # pointer to buffer
    movl $1, %edx          # number of bytes to read
    int $0x80              # call kernel

    # Process the character
    movb char_in, %al      # load the character into AL
    subb $1, %al           # subtract 1 from the character
    movb %al, char_in      # store the result back in the buffer

    # Write the modified character to stdout (file descriptor 1)
    movl $4, %eax          # syscall number for sys_write (4)
    movl $1, %ebx          # file descriptor 1 (stdout)
    movl $char_in, %ecx    # pointer to buffer
    movl $1, %edx          # number of bytes to write
    int $0x80              # call kernel

    # Exit the program
    movl $1, %eax          # syscall number for sys_exit (1)
    xorl %ebx, %ebx        # exit code 0
    int $0x80              # call kernel
