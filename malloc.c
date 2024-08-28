#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void){
char* x = malloc(50 * sizeof(char));

if (x == NULL){
    return 1;
}
printf("Escreva a frase a ser reescrita:");
fgets(x,50,stdin);

if (x[strlen(x) - 1] != '\n'){
    char* tmp = realloc(x, 100 * sizeof(char));
    if (x == NULL){
        return 1;
        free(x);
}
x = tmp;
fgets(x + 49,51,stdin);
}
printf("Sua frase é: %s\n", x);

free(x);

return 0;
}