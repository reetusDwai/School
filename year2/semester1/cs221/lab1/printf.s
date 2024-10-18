# printf.s
# This program adds 48 and 29 and then outputs the sum in hex. It
# uses stdlib.
# gcc -no-pie echo.s -o echo
# prevents missing .note.GNU-stack error
.section .note.GNU-stack,"",@progbits
#.extern putchar
.section .data
num1: .word 48
num2: .word 29
# The h in the format specifier is a length parameter.
# Printf expects a unsigned short int.
format: .string "result = %04hx\n\0"
.section .text
.global main
main:
# Load the values into registers
movl num1, %eax
movl num2, %ebx
# Add the values
addl %ebx, %eax
# save the callee of main, call to printf will wipe it out
push %rbp
# Call printf to print the result:
# printf("%04hx\n", sum)
# loads effective address of format string
# into first argument register
lea format, %rdi
# move value we want to print into the
# second argument register
movl %eax, %esi
call printf
# Restore the callee that was overwritten by
# call to printf
pop %rbp
ret
