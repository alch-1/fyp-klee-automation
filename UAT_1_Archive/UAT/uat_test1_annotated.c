#include "/home/klee/klee_src/include/klee/klee.h"
#include"stdio.h"
void main ()
{
    char s[20];
klee_make_symbolic(s, sizeof(s), "s");
    printf("Enter the string?");
/*    scanf("%s",s);
*/    printf("You entered %s",s);
}
