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
    movq $2, %rdx # number of bytes to read
    syscall

    # Convert buffer into a number
    movzbw buffer, %ax # Loads the first digit(10s place) into AX 
    # movzbw means move a byte into a word with higher order bits in the word being zero
    sub $'0', %ax # Converts the ascii to an int by subtracting the ascii character 0
    movw $10, %bx # Puts 10 into BX for multiplying
    # Multiplies AX by BX and stores it in AX
    mulw %bx

    # Convert second byte to a number
    # Loads the second digit into BX
    movzbw buffer+1, %bx
    sub $'0', %bx
    addw %bx, %ax # Adds the second digit to the first digit giving us the correct digit
    movw %ax, buffer # Moves number back to buffer

    # compute f(x)
    movw buffer, %ax # Loads the bytes from buffer into AX
    movw $27, %bx # Puts 27 into BX so that we can multiply
    # Multiplies AX by BX and stores it in AX
    mulw %bx 
    addw $17, %ax # Adds 17 to AX
    movw %ax, buffer # Store result back into buffer

    # Write the modified character to stdout
    movq $1, %rax # syscall number for sys_write (1)
    movq $1, %rdi # file descriptor for stdout (1)
    movq $buffer, %rsi # pointer to the buffer
    movq $4, %rdx # number of bytes to write
    syscall
    # Exit the program
    movq $60, %rax # syscall number for sys_exit (60)
    movq $0, %rdi # status = 0
    syscall
