#include<stdio.h>

// Global method declaration
int count_vowels(char []);
int check_vowel(char);

int main()
{
    printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");
    char aj[100];
    int mj;

    printf("\n\nEnter a string :   ");
    gets(aj);   // inputting a string from user

    mj = count_vowels(aj);  // function call

    printf("\n\nNumber of vowels in string \'%s\' is: %d", aj, mj);
    printf("\n\n\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}

/*
    Collecting the input string in char array 
    adi[], all at a time
*/
int count_vowels(char adi[]) 
{
    int count = 0, c= 0, flag = 0;
    char d;
    do
    {
        /*
            Storing each character of string in 
            char 'd' one at a time
        */
        d = adi[c]; 
        /*
            Calling function to check if char is vowel or not
        */
        flag = check_vowel(d); 

        if(flag ==1)    // if the char is vowel
        {
            count++;    // increment the count of the vowel
        }
        c++;    // updating the string character to be checked
    }while(d != '\0');  // terminating condition till it reaches the end of the string

    return count;
}

int check_vowel(char ajj)
{
    if(ajj >= 'A' && ajj <= 'Z')  // if the char is uppercase
        ajj = ajj+'a' - 'A';    // converting to lowercase using the ASCII values

    // if the char is any of the vowel
    if(ajj == 'a' || ajj == 'e' || ajj == 'i' || ajj == 'o' || ajj == 'u')
        return 1;   // making flag=1

    return 0;   // if not a vowel, flag remains 0
}
