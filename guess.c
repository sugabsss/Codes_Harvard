#include <cs50.h>
#include <stdio.h>


int main (void){
    int number = 3;
    int guess;

    do {
        guess = get_int("Advinhe o numero que estou pensando!\n");
        if (number == guess){
            printf("Parabéns!era esse mesmo!\n");}
        else {
            printf("Essa não..., tente novamente!\n");
        }
    }
    while (guess != number);
    return 0;
     
}
