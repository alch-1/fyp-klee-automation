#include "/home/klee/klee_src/include/klee/klee.h"
#include "stdio.h"

int main() {    

    int number1, sum;
klee_make_symbolic(&number1, sizeof(number1), "number1");

    printf("Enter two integers: ");
    
    int number2 = 2;
klee_make_symbolic(&number2, sizeof(number2), "number2");

    sum = number1 + number2;      
    
    printf("%d + %d = %d", number1, number2, sum);
    return 0;
}
