# fx.s
# Read two decimal digits from stdin and interpret that input as an integer between 0 and 99, inclusive
# Compute 27x + 17, where x is the provided integer
# Print the input value, the result in decimal and hexadecimal like this:
# x = 19 : f(x) = 530 or 0x212
# gcc -no-pie fx.s -o fx 
# this line prevents a loader warning
.section .note.GNU-stack,"",@progbits
.section .data
    .comm buffer, 4 # Allocate 4 byte for the result of the function
format: .string "x = %d : f(x) = %d or 0x%x\n\0"
.section .text
    .global main 
# This program does not use stdlib. The linker recognizes _start
# as the beginning of execution.
main:
    # Read two characters from stdin
    movq $0, %rax # syscall number for sys_read (0)
    movq $0, %rdi # file descriptor for stdin (0)
    movq $buffer, %rsi # pointer to the buffer
    movq $2, %rdx # number of bytes to read
    syscall

    # Convert buffer into a number
    movzbw buffer, %ax # Loads the first digit(10s place) into AX 
    # movzbw means move a byte into a word with higher order bits in the word being zero
    subw $'0', %ax # Converts the ascii to an int by subtracting the ascii character 0
    movw $10, %bx # Puts 10 into BX for multiplying
    # Multiplies AX by BX and stores it in AX
    mulw %bx

    # Convert second byte to a number
    # Loads the second digit into BX
    movzbw buffer+1, %bx
    subw $'0', %bx
    addw %bx, %ax # Adds the second digit to the first digit giving us the correct digit
    movw %ax, buffer # Moves number back to buffer

    # store the starting input
    movzx buffer, %esi

    # compute f(x)
    movw buffer, %ax # Loads the bytes from buffer into AX
    movw $27, %bx # Puts 27 into BX so that we can multiply
    # Multiplies AX by BX and stores it in AX
    mulw %bx 
    addw $17, %ax # Adds 17 to AX
    movw %ax, buffer # Store result back into buffer

    # save the callee of main, call to printf will wipe it out
    push %rbp

    # loads effective address of format string
    # into first argument register
    lea format, %rdi
    # move value we want to print into the
    # all the arguments
    movl buffer, %edx
    movl buffer, %ecx
    
    # calling printf
    call printf

    # Restore the callee that was overwritten by
    # call to printf
    pop %rbp
    ret

    # Exit the program
    movq $60, %rax # syscall number for sys_exit (60)
    movq $0, %rdi # status = 0
    syscall
