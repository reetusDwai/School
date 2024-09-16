# Prompt
# Make the following using ATT assembly

# Read two decimal digits from stdin and interpret that input as an integer between 0 an
# 99, inclusive. Compute 27x + 17, where x is the provided integer. Print the input value, the result in
# decimal and hexadecimal like this:
# x = 19 : f(x) = 530 or 0x212
# Spacing matters.

# Aside from the fact that there is an error and it won't compile, the code looks like it would 
# work and the comments explain what it is doing properly

.section .data
    prompt:     .asciz  "Enter a decimal value: "
    result:     .asciz  "x = %d : f(x) = %d or 0x%x\n"

.section .bss
    .lcomm input_buffer, 4  # buffer for reading input

.section .text
    .global _start

_start:
    # Print prompt message
    mov $1, %rax            # syscall: write
    mov $1, %rdi            # file descriptor: stdout
    mov $prompt, %rsi       # address of message to write
    mov $20, %rdx           # length of message
    syscall                 # invoke syscall

    # Read input from stdin (2-digit decimal number)
    mov $0, %rax            # syscall: read
    mov $0, %rdi            # file descriptor: stdin
    mov $input_buffer, %rsi # buffer to store input
    mov $4, %rdx            # max length of input (including newline)
    syscall                 # invoke syscall

    # Convert ASCII input to integer
    mov $0, %rbx            # clear rbx to store the result (x)
    mov input_buffer, %rsi  # point to input_buffer

    # Convert first digit (tens place)
    movb (%rsi), %al        # load first byte
    sub $48, %al            # convert ASCII to digit
    imul $10, %al           # multiply by 10
    add %al, %bl            # store in lower byte of rbx

    # Convert second digit (ones place)
    movb 1(%rsi), %al       # load second byte
    sub $48, %al            # convert ASCII to digit
    add %al, %bl            # add to the result in bl

    # Compute f(x) = 27x + 17
    mov %rbx, %rax          # move x (rbx) to rax for calculation
    imul $27, %rax          # multiply by 27
    add $17, %rax           # add 17

    # Prepare for printing the result
    mov %rbx, %rsi          # pass x (stored in bl) to second argument for printf
    mov %rax, %rdx          # pass result to third argument for printf
    mov %rax, %r8           # copy result to r8 for hexadecimal printing

    # Print the result
    mov $1, %rax            # syscall: write
    mov $1, %rdi            # file descriptor: stdout
    lea result(%rip), %rsi  # format string
    mov $input_buffer, %rdx # address of buffer (x value)
    syscall                 # invoke syscall

    # Exit
    mov $60, %rax           # syscall: exit
    xor %rdi, %rdi          # exit code 0
    syscall                 # invoke syscall
